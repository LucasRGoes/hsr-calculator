"""These are the enemy models of the application. They hold important data and
methods concerning calculations of HSR's enemies.
"""

from enum import Enum, auto
from typing import List, NamedTuple

from .. import terminology


class EnemyTier(Enum):
    """Represents HSR's enemy tiers.

    Extends:
        Enum
    """
    NORMAL = auto()
    ELITE = auto()
    BOSS = auto()
    ECHO_OF_WAR = auto()


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
    """The EnemyStats class holds stats of HSR's enemies.

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


class BaseEnemy:
    """The BaseEnemy class holds stats and other information regarding HSR's
    enemies.
    """

    def __init__(
        self,
        name: str,
        tier: EnemyTier,
        damage_type: terminology.Element,
        weaknesses: List[terminology.Element],
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
        """BaseEnemy constructor.

        Arguments:
            name {str} -- The enemy's name
            tier {EnemyTier} -- The enemy's tier
            damage_type {terminology.Element} -- The enemy's damage type
            weaknesses {List[terminology.Element]} -- The enemy's list of
            elemental weaknesses
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

    def __eq__(self, other: 'BaseEnemy') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {BaseEnemy} -- BaseEnemy to be compared

        Returns:
            bool -- if the Enemies are equal or not
        """
        if isinstance(other, BaseEnemy):
            return self._name == other._name \
                and self._tier == other._tier \
                and self._damage_type == other._damage_type \
                and self._weaknesses == other._weaknesses \
                and self._toughness == other._toughness \
                and self._base_stats == other._base_stats

        return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the BaseEnemy
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
            str -- string representation of the BaseEnemy
        """
        return (
            f'{self.name} ({self.tier_as_str}) - {self.damage_type_as_str}'
        )

    @property
    def name(self) -> str:
        """Getter for the name parameter.

        Returns:
            str -- the name parameter
        """
        return self._name

    @property
    def tier(self) -> EnemyTier:
        """Getter for the tier parameter.

        Returns:
            EnemyTier -- the tier parameter
        """
        return self._tier

    @property
    def tier_as_str(self) -> str:
        """Getter for the tier parameter as a string.

        Returns:
            str -- the tier parameter
        """
        return self._tier.name.capitalize()

    @property
    def tier_as_int(self) -> int:
        """Getter for the tier parameter as an integer.

        Returns:
            int -- the tier parameter
        """
        return self._tier.value

    @property
    def damage_type(self) -> terminology.Element:
        """Getter for the damage_type parameter.

        Returns:
            terminology.Element -- the damage_type parameter
        """
        return self._damage_type

    @property
    def damage_type_as_str(self) -> str:
        """Getter for the damage_type parameter as a string.

        Returns:
            str -- the damage_type parameter
        """
        return self._damage_type.name.capitalize()

    @property
    def damage_type_as_int(self) -> int:
        """Getter for the damage_type parameter as an integer.

        Returns:
            int -- the damage_type parameter
        """
        return self._damage_type.value

    @property
    def weaknesses(self) -> List[terminology.Element]:
        """Getter for the weaknesses parameter.

        Returns:
            List[terminology.Element] -- the weaknesses parameter
        """
        return self._weaknesses

    @property
    def weaknesses_as_str(self) -> str:
        """Getter for the weaknesses parameter as a string.

        Returns:
            str -- the weaknesses parameter
        """
        return ', '.join(map(lambda w: w.name.capitalize(), self._weaknesses))

    @property
    def toughness(self) -> int:
        """Getter for the toughness parameter.

        Returns:
            int -- the toughness parameter
        """
        return self._toughness

    @property
    def hit_points(self) -> float:
        """Getter for the base_stats.hit_points parameter.

        Returns:
            float -- the hit_points parameter
        """
        return self._base_stats.hit_points

    @property
    def attack(self) -> float:
        """Getter for the base_stats.attack parameter.

        Returns:
            float -- the attack parameter
        """
        return self._base_stats.attack

    @property
    def defense(self) -> float:
        """Getter for the base_stats.defense parameter.

        Returns:
            float -- the defense parameter
        """
        return self._base_stats.defense

    @property
    def speed(self) -> float:
        """Getter for the base_stats.speed parameter.

        Returns:
            float -- the speed parameter
        """
        return self._base_stats.speed

    @property
    def effect_hit_rate(self) -> float:
        """Getter for the base_stats.effect_hit_rate parameter.

        Returns:
            float -- the effect_hit_rate parameter
        """
        return self._base_stats.effect_hit_rate

    @property
    def effect_res(self) -> float:
        """Getter for the base_stats.effect_res parameter.

        Returns:
            float -- the effect_res parameter
        """
        return self._base_stats.effect_res

    @property
    def damage_res(self) -> EnemyDamageResistences:
        """Getter for the base_stats.damage_res parameter.

        Returns:
            EnemyDamageResistences -- the damage_res parameter
        """
        return self._base_stats.damage_res

    @property
    def debuff_res(self) -> EnemyDebuffResistences:
        """Getter for the base_stats.debuff_res parameter.

        Returns:
            EnemyDebuffResistences -- the debuff_res parameter
        """
        return self._base_stats.debuff_res
