"""These are the character models of the application. They hold important data
and methods concerning calculations of HSR's characters.
"""

from typing import NamedTuple

from .. import terminology


class CharacterStats(NamedTuple):
    """The CharacterStats class holds stats of HSR's characters.

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


class BaseCharacter:
    """The BaseCharacter class holds stats and other information regarding
    HSR's characters.
    """

    def __init__(
        self,
        name: str,
        rarity: terminology.Rarity,
        path: terminology.Path,
        combat_type: terminology.Element,
        hit_points: float,
        attack: float,
        defense: float,
        speed: float,
        max_energy: int,
        traces_stats: CharacterStats
    ):
        """BaseCharacter constructor.

        Arguments:
            name {str} -- The character's name
            rarity {terminology.Rarity} -- The character's rarity, ranging from
            3* to 5*
            path {terminology.Path} -- The character's path
            combat_type {terminology.Element} -- The character's combat type
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

    def __eq__(self, other: 'BaseCharacter') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {BaseCharacter} -- BaseCharacter to be compared

        Returns:
            bool -- if the Characters are equal or not
        """
        if isinstance(other, BaseCharacter):
            return self._name == other._name \
                and self._rarity == other._rarity \
                and self._path == other._path \
                and self._combat_type == other._combat_type \
                and self._base_stats == other._base_stats \
                and self._max_energy == other._max_energy

        return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the BaseCharacter
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
            str -- string representation of the BaseCharacter
        """
        return (
            f'{self.name} ({self.rarity_as_str}) - {self.path_as_str} - '
            f'{self.combat_type_as_str}'
        )

    @property
    def name(self) -> str:
        """Getter for the name parameter.

        Returns:
            str -- the name parameter
        """
        return self._name

    @property
    def rarity(self) -> terminology.Rarity:
        """Getter for the rarity parameter.

        Returns:
            terminology.Rarity -- the rarity parameter
        """
        return self._rarity

    @property
    def rarity_as_str(self) -> str:
        """Getter for the rarity parameter as a string.

        Returns:
            str -- the rarity parameter
        """
        if self._rarity is terminology.Rarity.THREE_STARS:
            return '3*'

        if self._rarity is terminology.Rarity.FOUR_STARS:
            return '4*'

        return '5*'

    @property
    def rarity_as_int(self) -> int:
        """Getter for the rarity parameter as an integer.

        Returns:
            int -- the rarity parameter
        """
        return self._rarity.value

    @property
    def path(self) -> terminology.Path:
        """Getter for the path parameter.

        Returns:
            terminology.Path -- the path parameter
        """
        return self._path

    @property
    def path_as_str(self) -> str:
        """Getter for the path parameter as a string.

        Returns:
            str -- the path parameter
        """
        return self._path.name.capitalize()

    @property
    def path_as_int(self) -> int:
        """Getter for the path parameter as an integer.

        Returns:
            int -- the path parameter
        """
        return self._path.value

    @property
    def combat_type(self) -> terminology.Element:
        """Getter for the combat_type parameter.

        Returns:
            terminology.Element -- the combat_type parameter
        """
        return self._combat_type

    @property
    def combat_type_as_str(self) -> str:
        """Getter for the combat_type parameter as a string.

        Returns:
            str -- the combat_type parameter
        """
        return self._combat_type.name.capitalize()

    @property
    def combat_type_as_int(self) -> int:
        """Getter for the combat_type parameter as an integer.

        Returns:
            int -- the combat_type parameter
        """
        return self._combat_type.value

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
    def crit_rate(self) -> float:
        """Getter for the base_stats.crit_rate parameter.

        Returns:
            float -- the crit_rate parameter
        """
        return self._base_stats.crit_rate

    @property
    def crit_damage(self) -> float:
        """Getter for the base_stats.crit_damage parameter.

        Returns:
            float -- the crit_damage parameter
        """
        return self._base_stats.crit_damage

    @property
    def break_effect(self) -> float:
        """Getter for the base_stats.break_effect parameter.

        Returns:
            float -- the break_effect parameter
        """
        return self._base_stats.break_effect

    @property
    def outgoing_healing_boost(self) -> float:
        """Getter for the base_stats.outgoing_healing_boost parameter.

        Returns:
            float -- the outgoing_healing_boost parameter
        """
        return self._base_stats.outgoing_healing_boost

    @property
    def energy_regeneration_rate(self) -> float:
        """Getter for the base_stats.energy_regeneration_rate parameter.

        Returns:
            float -- the energy_regeneration_rate parameter
        """
        return self._base_stats.energy_regeneration_rate

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
    def damage_boost(self) -> float:
        """Getter for the base_stats.damage_boost parameter.

        Returns:
            float -- the damage_boost parameter
        """
        return self._base_stats.damage_boost

    @property
    def max_energy(self) -> int:
        """Getter for the max_energy parameter.

        Returns:
            int -- the max_energy parameter
        """
        return self._max_energy

    @property
    def traces_stats(self) -> CharacterStats:
        """Getter for the traces_stats parameter.

        Returns:
            CharacterStats -- the traces_stats parameter
        """
        return self._traces_stats
