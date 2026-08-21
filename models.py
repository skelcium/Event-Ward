from pydantic import BaseModel, Field

# activePlayer
class Ability(BaseModel):
    abilityLevel: int | None = None
    displayName: str
    id: str
    rawDescription: str
    rawDisplayName: str

class Passive(BaseModel):
    displayName: str
    id: str
    rawDescription: str
    rawDisplayName: str

class Abilities(BaseModel):
    e: Ability = Field(alias='E')
    passive: Ability = Field(alias='Passive')
    q: Ability = Field(alias='Q')
    r: Ability = Field(alias='R')
    w: Ability = Field(alias='W')

class ChampionStats(BaseModel):
    abilityHaste: float
    abilityPower: float
    armor: float
    armorPenetrationFlat: float
    armorPenetrationPercent: float
    attackDamage: float
    attackRange: float
    attackSpeed: float
    bonusArmorPenetrationPercent: float
    bonusMagicPenetrationPercent: float
    critChance: float
    critDamage: float
    currentHealth: float
    healShieldPower: float
    healthRegenRate: float
    lifeSteal: float
    magicLethality: float
    magicPenetrationFlat: float
    magicPenetrationPercent: float
    magicResist: float
    maxHealth: float
    moveSpeed: float
    omnivamp: float
    physicalLethality: float
    physicalVamp: float
    resourceMax: float
    resourceRegenRate: float
    resourceType: str
    resourceValue: float
    spellVamp: float
    tenacity: float

class Rune(BaseModel):
    displayName: str | None = None
    id: int
    rawDescription: str
    rawDisplayName: str | None = None

# Some Game Modes disallow rune pages, hence the many Nones.
class FullRunes(BaseModel):
    generalRunes: list[Rune] | None = None
    keystone: Rune | None = None
    primaryRuneTree: Rune | None = None
    secondaryRuneTree: Rune | None = None
    statRunes: list[Rune] | None = None

class ActivePlayer(BaseModel):
    abilities: Abilities
    championStats: ChampionStats
    currentGold: float
    fullRunes: FullRunes
    level: int
    riotId: str
    riotIdGameName: str
    riotIdTagLine: str
    summonerName: str
    teamRelativeColors: bool

# allPlayers

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
    EventID: int
    EventName: str
    EventTime: float
    Assisters: list[str] | None = None
    KillerName: str | None = None
    VictimName: str | None = None
    DragonType: str | None = None
    Stolen: str | None = None
    TurretKilled: str | None = None
    InhibKilled: str | None = None
    InhibRespawningSoon: str | None = None
    InhibRespawned: str | None = None
    KillStreak: int | None = None
    Acer: str | None = None
    AcingTeam: str | None = None
    Result: str | None = None
    Recipient: str | None = None

class Events(BaseModel):
    events: list[Event] = Field(alias='Events')

class EventRoot(BaseModel):
    events: Events

# Types of events
class GameStartEvent(BaseModel):
    EventID: int
    EventTime: float

class MinionsSpawningEvent(BaseModel):
    EventID: int
    EventTime: float

class FirstBloodEvent(BaseModel):
    EventID: int
    EventTime: float
    Recipient: str

class FirstBrickEvent(BaseModel):
    EventID: int
    EventTime: float
    KillerName: str

class ChampionKillEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    KillerName: str
    VictimName: str

class MultikillEvent(BaseModel):
    EventID: int
    EventTime: float
    KillStreak: int
    KillerName: str

class AceEvent(BaseModel):
    EventID: int
    EventTime: float
    Acer: str
    AcingTeam: "ORDER | CHAOS"

class TurretKilledEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    KillerName: str
    TurretKilled: str

class InhibKilledEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    InhibKilled: str
    KillerName: str

class InhibRespawningSoonEvent(BaseModel):
    EventID: int
    EventTime: float
    InhibRespawningSoon: str

class InhibRespawnedEvent(BaseModel):
    EventID: int
    EventTime: float
    InhibRespawned: str

class DragonKillEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    DragonType: str
    KillerName: str
    Stolen: bool

class HeraldKillEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    KillerName: str
    Stolen: bool

class BaronKillEvent(BaseModel):
    EventID: int
    EventTime: float
    Assisters: list[str] = []
    KillerName: str
    Stolen: bool

class GameEndEvent(BaseModel):
    EventID: int
    EventTime: float
    Result: "WIN | LOSS"

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
}

# gameData