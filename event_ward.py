from typing import get_type_hints
import requests
import urllib3
import models
from pydantic import ValidationError
import logging
import time

class EventWard:
    def __init__(self, suppress_cached_events: bool = True, poll_interval: float = 0.1):
        self.suppress_cached_events = suppress_cached_events
        self.poll_interval = poll_interval
        self.first_run = True
        self.should_shutdown = False
        #self.api_url = 'https://127.0.0.1:2999/liveclientdata/allgamedata'

        # Endpoints
        self.base_url = 'https://127.0.0.1:2999/liveclientdata'
        self.active_player_endpoint = 'activeplayer'
        self.event_data_endpoint = 'eventdata'
        self.active_player_abilities_endpoint = 'activeplayerabilities'
        self.active_player_runes_endpoint = 'activeplayerrunes'
        self.player_list_endpoint = 'playerlist'

        #Query Endpoints
        self.player_scores_query_endpoint = "playerscores?riotId={}"
        self.player_summoner_spells_query_endpoint = "playersummonerspells?riotId={}"
        self.player_main_runes_query_endpoint = "playermainrunes?riotId={}"
        self.player_items_query_endpoint = "playeritems?riotId={}"

        self.amount_of_events = 0
        self.current_event_index = -1
        self.callback_funcs = []

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        self.session = requests.Session()
        self.session.verify = False

    def watch(self, func):
        self.callback_funcs.append(func)

    def process_latest_events(self):
        try:
            data = self.session.get(self.make_url(self.event_data_endpoint)).json()
            logging.debug(f"Processing events {data}")
        except:
            return

        try:
            events = models.Events.model_validate(data).events
        except KeyError:
            # Events not yet available
            logging.debug("Events not yet available, retrying...")
            return
        except ValidationError:
            # Game not fully started
            logging.debug("Game not fully started, retrying...")
            return


        self.amount_of_events = len(events)

        if self.suppress_cached_events and self.first_run:
            self.first_run = False
            self.current_event_index = self.amount_of_events - 1

        if self.amount_of_events == 0:
            return

        if self.current_event_index < self.amount_of_events - 1:
            # Iterate through latest events
            for event in events[self.current_event_index + 1:]:
                corresponding_model = models.event_ties[event.event_name]

                # Check if any of the latest events are registered as callbacks
                for callback in self.callback_funcs:
                    hints = get_type_hints(callback)

                    for key, value in hints.items():
                        if value == corresponding_model:
                            callback(corresponding_model(**event.model_dump(by_alias=True)))

            self.current_event_index = self.amount_of_events - 1

        # Detect new game
        elif self.current_event_index > self.amount_of_events - 1:
            logging.info("New game detected!")
            self.current_event_index = -1

    def get_active_player(self):
        data = self.session.get(self.make_url(self.active_player_endpoint)).json()
        return models.ActivePlayer.model_validate(data)

    def get_active_player_abilities(self):
        data = self.session.get(self.make_url(self.active_player_abilities_endpoint)).json()
        return models.Abilities.model_validate(data)

    def get_active_player_runes(self):
        data = self.session.get(self.make_url(self.active_player_runes_endpoint)).json()
        return models.FullRunes.model_validate(data)

    def get_player_list(self):
        data = self.session.get(self.make_url(self.player_list_endpoint)).json()
        return models.AllPlayers(players=data)

    def get_player_scores(self, riot_id: str):
        data = self.session.get(self.make_url(self.player_scores_query_endpoint, riot_id)).json()
        return models.Score.model_validate(data)

    def get_player_summoner_spells(self, riot_id: str):
        data = self.session.get(self.make_url(self.player_summoner_spells_query_endpoint, riot_id)).json()
        return models.SummonerSpells.model_validate(data)

    def get_player_main_runes(self, riot_id: str):
        data = self.session.get(self.make_url(self.player_main_runes_query_endpoint, riot_id)).json()
        return models.FullRunes.model_validate(data)

    def get_player_items(self, riot_id: str):
        data = self.session.get(self.make_url(self.player_items_query_endpoint, riot_id)).json()
        return models.Item.model_validate(data)

    def make_url(self, endpoint: str, args: str | None = None):
        if args is None:
            return f"{self.base_url}/{endpoint}"
        else:
            return f"{self.base_url}/{endpoint.format(args)}"

    def start(self):
        while not self.should_shutdown:
            self.process_latest_events()
            time.sleep(self.poll_interval)

    def shutdown(self):
        self.should_shutdown = True
        self.session.close()