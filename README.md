# Event Ward
A callback-based event listener for League of Legends. Utilizes the official [Live Client Data API](https://developer.riotgames.com/docs/lol#game-client-api_live-client-data-api), and Pydantic models for easy means of accessing data.

⚠️ **Note:** This library is far from complete.

## Usage
models.py contains several events classes that can be listened to, such as in the example below:

```python
import event_ward
import models

ward = event_ward.EventWard()

active_player: models.ActivePlayer
my_name: str


@ward.watch
def game_started(game_start_event: models.GameStartEvent):
    global active_player, my_name

    active_player = ward.get_active_player()
    my_name = active_player.riot_id_game_name

    print(f"The game has started! Good luck {my_name}!")

@ward.watch
def kill(kill_event: models.ChampionKillEvent):
    if my_name == kill_event.killer_name:
        print(f"You killed {kill_event.victim_name}!")

@ward.watch
def tower_destroyed(brick_event: models.FirstBrickEvent):
    minutes, seconds = divmod(int(brick_event.event_time), 60)
    print(f"First tower destroyed at {minutes} minutes and {seconds} seconds.")

@ward.watch
def game_ended(game_end_event: models.GameEndEvent):
    player_list = ward.get_playerlist()

    print("Match KDA Summary: ")

    for player in player_list.players:
        print(f"{player.champion_name} - {player.scores.kills} / {player.scores.deaths} / {player.scores.assists}")

while True:
    ward.process_latest_events()
```