from pydantic import BaseModel, Field, RootModel
from typing import Literal

# activePlayer
class Ability(BaseModel):
    ability_level: int | None = Field(default=None, alias='abilityLevel')
    display_name: str = Field(alias='displayName')
    id: str
    raw_description: str = Field(alias='rawDescription')
    raw_display_name: str = Field(alias='rawDisplayName')

class Passive(BaseModel):
    display_name: str = Field(alias='displayName')
    id: str
    raw_description: str = Field(alias='rawDescription')
    raw_display_name: str = Field(alias='rawDisplayName')

class Abilities(BaseModel):
    e: Ability = Field(alias='E')
    passive: Passive = Field(alias='Passive')
    q: Ability = Field(alias='Q')
    r: Ability = Field(alias='R')
    w: Ability = Field(alias='W')

class ChampionStats(BaseModel):
    ability_haste: float = Field(alias='abilityHaste')
    ability_power: float = Field(alias='abilityPower')
    armor: float
    armor_penetration_flat: float = Field(alias='armorPenetrationFlat')
    armor_penetration_percent: float = Field(alias='armorPenetrationPercent')
    attack_damage: float = Field(alias='attackDamage')
    attack_range: float = Field(alias='attackRange')
    attack_speed: float = Field(alias='attackSpeed')
    bonus_armor_penetration_percent: float = Field(alias='bonusArmorPenetrationPercent')
    bonus_magic_penetration_percent: float = Field(alias='bonusMagicPenetrationPercent')
    crit_chance: float = Field(alias='critChance')
    crit_damage: float = Field(alias='critDamage')
    current_health: float = Field(alias='currentHealth')
    heal_shield_power: float = Field(alias='healShieldPower')
    health_regen_rate: float = Field(alias='healthRegenRate')
    life_steal: float = Field(alias='lifeSteal')
    magic_lethality: float = Field(alias='magicLethality')
    magic_penetration_flat: float = Field(alias='magicPenetrationFlat')
    magic_penetration_percent: float = Field(alias='magicPenetrationPercent')
    magic_resist: float = Field(alias='magicResist')
    max_health: float = Field(alias='maxHealth')
    move_speed: float = Field(alias='moveSpeed')
    omnivamp: float
    physical_lethality: float = Field(alias='physicalLethality')
    physical_vamp: float = Field(alias='physicalVamp')
    resource_max: float = Field(alias='resourceMax')
    resource_regen_rate: float = Field(alias='resourceRegenRate')
    resource_type: str = Field(alias='resourceType')
    resource_value: float = Field(alias='resourceValue')
    spell_vamp: float = Field(alias='spellVamp')
    tenacity: float

class Rune(BaseModel):
    display_name: str | None = Field(default=None, alias='displayName')
    id: int
    raw_description: str = Field(alias='rawDescription')
    raw_display_name: str | None = Field(default=None, alias='rawDisplayName')

# Some Game Modes disallow rune pages, hence the many Nones.
class FullRunes(BaseModel):
    general_runes: list[Rune] | None = Field(default=None, alias='generalRunes')
    keystone: Rune | None = None
    primary_rune_tree: Rune | None = Field(default=None, alias='primaryRuneTree')
    secondary_rune_tree: Rune | None = Field(default=None, alias='secondaryRuneTree')
    stat_runes: list[Rune] | None = Field(default=None, alias='statRunes')

class ActivePlayer(BaseModel):
    abilities: Abilities
    champion_stats: ChampionStats = Field(alias='championStats')
    current_gold: float = Field(alias='currentGold')
    full_runes: FullRunes | None = Field(alias='fullRunes')
    level: int
    riot_id: str = Field(alias='riotId')
    riot_id_game_name: str = Field(alias='riotIdGameName')
    riot_id_tag_line: str = Field(alias='riotIdTagLine')
    summoner_name: str = Field(alias='summonerName')
    team_relative_colors: bool = Field(alias='teamRelativeColors')

class Item(BaseModel):
    can_use: bool = Field(alias='canUse')
    consumable: bool
    count: int
    display_name: str = Field(alias='displayName')
    item_id: int = Field(alias='itemID')
    price: int
    raw_description: str = Field(alias='rawDescription')
    raw_display_name: str = Field(alias='rawDisplayName')
    slot: int

class Score(BaseModel):
    assists: int
    creep_score: int = Field(alias='creepScore')
    deaths: int
    kills: int
    ward_score: float = Field(alias='wardScore')

class SummonerSpell(BaseModel):
    display_name: str = Field(alias='displayName')
    raw_description: str = Field(alias='rawDescription')
    raw_display_name: str = Field(alias='rawDisplayName')

class SummonerSpells(BaseModel):
    summoner_spell_one: SummonerSpell = Field(alias='summonerSpellOne')
    summoner_spell_two: SummonerSpell = Field(alias='summonerSpellTwo')

class Player(BaseModel):
    champion_name: str = Field(alias='championName')
    is_bot: bool = Field(alias='isBot')
    is_dead: bool = Field(alias='isDead')
    items: list[Item]
    level: int
    position: str
    raw_champion_name: str = Field(alias='rawChampionName')
    raw_skin_name: str = Field(alias='rawSkinName')
    respawn_timer: float = Field(alias='respawnTimer')
    riot_id: str = Field(alias='riotId')
    riot_id_game_name: str = Field(alias='riotIdGameName')
    riot_id_tag_line: str = Field(alias='riotIdTagLine')
    runes: FullRunes | None
    scores: Score
    skin_id: int = Field(alias='skinID')
    skin_name: str = Field(alias='skinName')
    summoner_name: str = Field(alias='summonerName')
    summoner_spells: SummonerSpells = Field(alias='summonerSpells')
    team: str

# allPlayers
class AllPlayers(RootModel[list[Player]]):
    pass

"""
# events
class EventType(StrEnum):
    GAME_START = "GameStart"
    MINIONS_SPAWNING = "MinionsSpawning"
    CHAMPION_KILL = "ChampionKill"
    FIRST_BLOOD = "FirstBlood"
    FIRST_BRICK = "FirstBrick"
    MULTIKILL = "Multikill"
    ACE = "Ace"
    DRAGON_KILL = "DragonKill"
    HERALD_KILL = "HeraldKill"
    BARON_KILL = "BaronKill"
    TURRET_KILLED = "TurretKilled"
    INHIB_KILLED = "InhibKilled"
    INHIB_RESPAWNING_SOON = "InhibRespawningSoon"
    INHIB_RESPAWNED = "InhibRespawned"
    GAME_END = "GameEnd"
"""

class Event(BaseModel):
    event_id: int = Field(alias='EventID')
    event_name: str = Field(alias='EventName')
    event_time: float = Field(alias='EventTime')
    assisters: list[str] | None = Field(default=None, alias='Assisters')
    killer_name: str | None = Field(default=None, alias='KillerName')
    victim_name: str | None = Field(default=None, alias='VictimName')
    dragon_type: str | None = Field(default=None, alias='DragonType')
    stolen: bool | None = Field(default=None, alias='Stolen')
    turret_killed: str | None = Field(default=None, alias='TurretKilled')
    inhib_killed: str | None = Field(default=None, alias='InhibKilled')
    inhib_respawning_soon: str | None = Field(default=None, alias='InhibRespawningSoon')
    inhib_respawned: str | None = Field(default=None, alias='InhibRespawned')
    kill_streak: int | None = Field(default=None, alias='KillStreak')
    acer: str | None = Field(default=None, alias='Acer')
    acing_team: str | None = Field(default=None, alias='AcingTeam')
    result: str | None = Field(default=None, alias='Result')
    recipient: str | None = Field(default=None, alias='Recipient')

class Events(BaseModel):
    events: list[Event] = Field(alias='Events')

class EventRoot(BaseModel):
    events: Events

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

class PlayerItems(RootModel[list[Item]]):
    pass

class GameStats(BaseModel):
    game_mode: str = Field(alias='gameMode')
    game_time: float = Field(alias='gameTime')
    map_name: str = Field(alias='mapName')
    map_number: int = Field(alias='mapNumber')
    map_terrain: str = Field(alias='mapTerrain')

class AllGameData(BaseModel):
    active_player: ActivePlayer = Field(alias='activePlayer')
    all_players: list[Player] = Field(alias='allPlayers')
    event_root: Events = Field(alias='events')
    game_data: GameStats = Field(alias='gameData')

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

# gameData