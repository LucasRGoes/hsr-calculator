"""These are the Character models of the application. They hold important
data and methods concerning stats data of HSR's Characters.
"""

from typing import NamedTuple

from ..terminology import Element, Path, Rarity


class CharacterStats(NamedTuple):
    """The CharacterStats class holds stats and other information regarding
    HSR's characters stats.

    Extends:
        NamedTuple

    Arguments:
        hit_points {float} -- A character's Hit Points (HP)
        attack {float} -- A character's Attack (ATK)
        defense {float} -- A character's Defense (DEF)
        speed {float} -- A character's Speed (SPD)
        crit_rate {float} -- A character's CRIT Rate (CR)
        crit_damage {float} -- A character's CRIT DMG (CD)
        break_effect {float} -- A character's Break Effect (Break)
        outgoing_healing_boost {float} -- A character's Outgoing Healing Boost
        (OHB)
        energy_regeneration_rate {float} -- A character's Energy Regeneration
        Rate (ERR)
        effect_hit_rate {float} -- A character's Effect Hit Rate (EHR)
        effect_res {float} -- A character's Effect RES (RES)
        damage_boost {float} -- A character's DMG Boost (DMG)
    """
    hit_points: float = 0.0
    attack: float = 0.0
    defense: float = 0.0
    speed: float = 0.0
    crit_rate: float = 0.0
    crit_damage: float = 0.0
    break_effect: float = 0.0
    outgoing_healing_boost: float = 0.0
    energy_regeneration_rate: float = 0.0
    effect_hit_rate: float = 0.0
    effect_res: float = 0.0
    damage_boost: float = 0.0


class Character(object):
    """The Character class holds stats and other information regarding HSR's
    characters.
    """

    def __init__(
        self,
        name: str,
        rarity: Rarity,
        path: Path,
        combat_type: Element,
        hit_points: float,
        attack: float,
        defense: float,
        speed: float,
        max_energy: int,
        traces_stats: CharacterStats
    ):
        """Character constructor.

        Arguments:
            name {str} -- The character's name
            rarity {Rarity} -- The character's rarity, ranging from 3* to 5*
            path {Path} -- The character's path
            combat_type {Element} -- The character's combat type
            hit_points {float} -- The character's Hit Points (HP)
            attack {float} -- The character's Attack (ATK)
            defense {float} -- The character's Defense (DEF)
            speed {float} -- The character's Speed (SPD)
            max_energy {int} -- The character's Max Energy
            traces_stats {CharacterStats} -- The character's traces stats
        """
        self._name = name
        self._rarity = rarity
        self._path = path
        self._combat_type = combat_type
        self._base_stats = CharacterStats(
            hit_points=hit_points,
            attack=attack,
            defense=defense,
            speed=speed,
            crit_rate=5.0,
            crit_damage=50.0,
            energy_regeneration_rate=100.0
        )
        self._max_energy = max_energy
        self._traces_stats = traces_stats

    def __eq__(self, other: 'Character') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {Character} -- Character to be compared

        Returns:
            bool -- if the Characters are equal or not
        """
        if type(other) == Character:
            return self._name == other._name \
                and self._rarity == other._rarity \
                and self._path == other._path \
                and self._combat_type == other._combat_type \
                and self._base_stats == other._base_stats \
                and self._max_energy == other._max_energy

        else:
            return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the Character
        """
        return hash((
            self._name,
            self._rarity,
            self._path,
            self._combat_type,
            self._base_stats,
            self._max_energy
        ))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Character
        """
        return (
            f'{self.name} ({self.rarity_as_str}) - {self.path_as_str} - '
            f'{self.combat_type_as_str}'
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def rarity(self) -> Rarity:
        return self._rarity

    @property
    def rarity_as_str(self) -> str:
        if self._rarity is Rarity.THREE_STARS:
            return '3*'
        elif self._rarity is Rarity.FOUR_STARS:
            return '4*'
        elif self._rarity is Rarity.FIVE_STARS:
            return '5*'

    @property
    def rarity_as_int(self) -> int:
        return self._rarity.value

    @property
    def path(self) -> Path:
        return self._path

    @property
    def path_as_str(self) -> str:
        return self._path.name.capitalize()

    @property
    def path_as_int(self) -> int:
        return self._path.value

    @property
    def combat_type(self) -> Element:
        return self._combat_type

    @property
    def combat_type_as_str(self) -> str:
        return self._combat_type.name.capitalize()

    @property
    def combat_type_as_int(self) -> int:
        return self._combat_type.value

    @property
    def hit_points(self) -> float:
        return self._base_stats.hit_points

    @property
    def attack(self) -> float:
        return self._base_stats.attack

    @property
    def defense(self) -> float:
        return self._base_stats.defense

    @property
    def speed(self) -> float:
        return self._base_stats.speed

    @property
    def crit_rate(self) -> float:
        return self._base_stats.crit_rate

    @property
    def crit_damage(self) -> float:
        return self._base_stats.crit_damage

    @property
    def break_effect(self) -> float:
        return self._base_stats.break_effect

    @property
    def outgoing_healing_boost(self) -> float:
        return self._base_stats.outgoing_healing_boost

    @property
    def energy_regeneration_rate(self) -> float:
        return self._base_stats.energy_regeneration_rate

    @property
    def effect_hit_rate(self) -> float:
        return self._base_stats.effect_hit_rate

    @property
    def effect_res(self) -> float:
        return self._base_stats.effect_res

    @property
    def damage_boost(self) -> float:
        return self._base_stats.damage_boost

    @property
    def max_energy(self) -> int:
        return self._max_energy

    @property
    def traces_stats(self) -> CharacterStats:
        return self._traces_stats
