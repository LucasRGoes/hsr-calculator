"""These are the Enemy models of the application. They hold important data and
methods concerning stats data of HSR's Enemies.
"""

from enum import Enum
from typing import NamedTuple

from ..terminology import Element


class EnemyTier(Enum):
    """Represents HSR's enemy tiers.

    Extends:
        Enum
    """
    NORMAL = 1


class EnemyDamageResistences(NamedTuple):
    """The EnemyDamageResistences class holds information regarding HSR's enemy
    damage resistances.

    Extends:
        NamedTuple

    Arguments:
        physical {float} -- An enemy's Physical DMG RES
        fire {float} -- An enemy's Fire DMG RES
        ice {float} -- An enemy's Ice DMG RES
        lightning {float} -- An enemy's Lightning DMG RES
        wind {float} -- An enemy's Wind DMG RES
        quantum {float} -- An enemy's Quantum DMG RES
        imaginary {float} -- An enemy's Imaginary DMG RES
    """
    physical: float = 0.0
    fire: float = 0.0
    ice: float = 0.0
    lightning: float = 0.0
    wind: float = 0.0
    quantum: float = 0.0
    imaginary: float = 0.0


class EnemyDebuffResistences(NamedTuple):
    """The EnemyDebuffResistences class holds information regarding HSR's enemy
    debuff resistances.

    Extends:
        NamedTuple

    Arguments:
        bleed {float} -- An enemy's Bleed Debuff RES
        burn {float} -- An enemy's Burn Debuff RES
        frozen {float} -- An enemy's Frozen Debuff RES
        shock {float} -- An enemy's Shock Debuff RES
        wind_sheer {float} -- An enemy's Wind Sheer Debuff RES
        entanglement {float} -- An enemy's Entanglement Debuff RES
        imprisonment {float} -- An enemy's Inprisoment Debuff RES
        control_effect {float} -- An enemy's Control Effect Debuf RES
    """
    bleed: float = 0.0
    burn: float = 0.0
    frozen: float = 0.0
    shock: float = 0.0
    wind_sheer: float = 0.0
    entanglement: float = 0.0
    imprisonment: float = 0.0
    control_effect: float = 0.0


class EnemyStats(NamedTuple):
    """The EnemyStats class holds stats and other information regarding HSR's
    enemy stats.

    Extends:
        NamedTuple

    Arguments:
        hit_points {float} -- An enemy's Hit Points (HP)
        attack {float} -- An enemy's Attack (ATK)
        defense {float} -- An enemy's Defense (DEF)
        speed {float} -- An enemy's Speed (SPD)
        effect_hit_rate {float} -- An enemy's Effect Hit Rate (EHR)
        effect_res {float} -- An enemy's Effect RES (RES)
        damage_res {EnemyDamageResistences} -- An enemy's damage resistances
        debuff_res {EnemyDebuffResistences} -- An enemy's debuff resistances
    """
    hit_points: float = 0.0
    attack: float = 0.0
    defense: float = 0.0
    speed: float = 0.0
    effect_hit_rate: float = 0.0
    effect_res: float = 0.0
    damage_res: EnemyDamageResistences = EnemyDamageResistences()
    debuff_res: EnemyDebuffResistences = EnemyDebuffResistences()


class Enemy(object):
    """The Enemy class holds stats and other information regarding HSR's
    enemies.
    """

    def __init__(
        self,
        name: str,
        tier: EnemyTier,
        damage_type: Element,
        weaknesses: list[Element],
        toughness: int,
        hit_points: float,
        attack: float,
        defense: float,
        speed: float,
        effect_hit_rate: float,
        effect_res: float,
        damage_res: EnemyDamageResistences,
        debuff_res: EnemyDebuffResistences
    ):
        """Enemy constructor.

        Arguments:
            name {str} -- The enemy's name
            tier {EnemyTier} -- The enemy's tier
            damage_type {Element} -- The enemy's damage type
            weaknesses {list[Element]} -- The enemy's list of elemental
            weaknesses
            toughness {int} -- The enemy's toughness
            hit_points {float} -- The enemy's Hit Points (HP)
            attack {float} -- The enemy's Attack (ATK)
            defense {float} -- The enemy's Defense (DEF)
            speed {float} -- The enemy's Speed (SPD)
            effect_hit_rate {float} -- The enemy's Effect Hit Rate (EHR)
            effect_res {float} -- The enemy's Effect RES (RES)
            damage_res {EnemyDamageResistences} -- The enemy's damage
            resistances
            debuff_res {EnemyDebuffResistences} -- The enemy's debuff
            resistances
        """
        self._name = name
        self._tier = tier
        self._damage_type = damage_type
        self._weaknesses = weaknesses
        self._toughness = toughness
        self._base_stats = EnemyStats(
            hit_points=hit_points,
            attack=attack,
            defense=defense,
            speed=speed,
            effect_hit_rate=effect_hit_rate,
            effect_res=effect_res,
            damage_res=damage_res,
            debuff_res=debuff_res
        )

    def __eq__(self, other: 'Enemy') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {Enemy} -- Enemy to be compared

        Returns:
            bool -- if the Enemies are equal or not
        """
        if type(other) == Enemy:
            return self._name == other._name \
                and self._tier == other._tier \
                and self._damage_type == other._damage_type \
                and self._weaknesses == other._weaknesses \
                and self._toughness == other._toughness \
                and self._base_stats == other._base_stats

        else:
            return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the Enemy
        """
        return hash((
            self._name,
            self._tier,
            self._damage_type,
            self._weaknesses,
            self._toughness,
            self._base_stats
        ))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Enemy
        """
        return (
            f'{self.name} ({self.tier_as_str}) - {self.damage_type_as_str}'
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def tier(self) -> EnemyTier:
        return self._tier

    @property
    def tier_as_str(self) -> str:
        return self._tier.name.capitalize()

    @property
    def tier_as_int(self) -> int:
        return self._tier.value

    @property
    def damage_type(self) -> Element:
        return self._damage_type

    @property
    def damage_type_as_str(self) -> str:
        return self._damage_type.name.capitalize()

    @property
    def damage_type_as_int(self) -> int:
        return self._damage_type.value

    @property
    def weaknesses(self) -> list[Element]:
        return self._weaknesses

    @property
    def weaknesses_as_str(self) -> str:
        return map(lambda w: w.name.capitalize(), self._weaknesses).join(', ')

    @property
    def toughness(self) -> int:
        return self._toughness

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
    def effect_hit_rate(self) -> float:
        return self._base_stats.effect_hit_rate

    @property
    def effect_res(self) -> float:
        return self._base_stats.effect_res

    @property
    def damage_res(self) -> EnemyDamageResistences:
        return self._base_stats.damage_res

    @property
    def debuff_res(self) -> EnemyDebuffResistences:
        return self._base_stats.debuff_res
