from pydantic import BaseModel, Field
from typing import Literal

# Types of events
class GameStartEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')

class MinionsSpawningEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')

class FirstBloodEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    recipient: str = Field(alias='Recipient')

class FirstBrickEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    killer_name: str = Field(alias='KillerName')

class ChampionKillEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    killer_name: str = Field(alias='KillerName')
    victim_name: str = Field(alias='VictimName')

class MultikillEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    kill_streak: int = Field(alias='KillStreak')
    killer_name: str = Field(alias='KillerName')

class AceEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    acer: str = Field(alias='Acer')
    acing_team: Literal["Order", "Chaos"] = Field(alias='AcingTeam')

class TurretKilledEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    killer_name: str = Field(alias='KillerName')
    turret_killed: str = Field(alias='TurretKilled')

class InhibKilledEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    inhib_killed: str = Field(alias='InhibKilled')
    killer_name: str = Field(alias='KillerName')

class InhibRespawningSoonEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    inhib_respawning_soon: str = Field(alias='InhibRespawningSoon')

class InhibRespawnedEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    inhib_respawned: str = Field(alias='InhibRespawned')

class DragonKillEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    dragon_type: str = Field(alias='DragonType')
    killer_name: str = Field(alias='KillerName')
    stolen: bool = Field(alias='Stolen')

class HeraldKillEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    killer_name: str = Field(alias='KillerName')
    stolen: bool = Field(alias='Stolen')

class BaronKillEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] = Field(default_factory=list, alias='Assisters')
    killer_name: str = Field(alias='KillerName')
    stolen: bool = Field(alias='Stolen')

class GameEndEvent(BaseModel):
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    result: Literal["Win", "Lose"] = Field(alias='Result')

class HordeKill(BaseModel):
    assisters: list[str] = Field(alias='Assisters')
    event_id: int = Field(alias='EventID')
    event_time: float = Field(alias='EventTime')
    killer_name: str = Field(alias='KillerName')
    stolen: bool = Field(alias='Stolen')


# Tie event names to their corresponding pydantic class
event_ties = {
    'GameStart': GameStartEvent,
    'MinionsSpawning': MinionsSpawningEvent,
    'ChampionKill': ChampionKillEvent,
    'FirstBlood': FirstBloodEvent,
    'FirstBrick': FirstBrickEvent,
    'Multikill': MultikillEvent,
    'Ace': AceEvent,
    'DragonKill': DragonKillEvent,
    'HeraldKill': HeraldKillEvent,
    'BaronKill': BaronKillEvent,
    'TurretKilled': TurretKilledEvent,
    'InhibKilled': InhibKilledEvent,
    'InhibRespawningSoon': InhibRespawningSoonEvent,
    'InhibRespawned': InhibRespawnedEvent,
    'GameEnd': GameEndEvent,
    'HordeKill': HordeKill
}