# Event Ward
A callback based event listener for League of Legends. Utilizes the official [Live Client Data API](https://developer.riotgames.com/docs/lol#game-client-api_live-client-data-api), and Pydantic models for easy means of accessing data.

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
    my_name = active_player.riotIdGameName

    print(f"Game started at {game_start_event.EventTime}.")

@ward.watch
def kill(kill_event: models.ChampionKillEvent):
    if my_name == kill_event.KillerName:
        print(f"You killed {kill_event.VictimName}!")

@ward.watch
def tower_destroyed(brick_event: models.FirstBrickEvent):
    minutes, seconds = divmod(int(brick_event.EventTime), 60)
    print(f"First tower destroyed at {minutes} minutes and {seconds} seconds.")


while True:
    ward.process_latest_events()
```