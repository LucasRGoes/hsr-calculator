"""This module holds the Character class, used to describe a character fully
equipped and on a battle situation.
"""

from copy import deepcopy

from .characters import CharacterStats, BaseCharacter


class Character:
    """The Character class is used to describe a character fully equipped and
    on a battle situation.
    """

    def __init__(self, base_character: BaseCharacter):
        """Character constructor.

        Arguments:
            base_character {BaseCharacter} -- The base character
        """
        self._base_character = base_character

        self._character_stats = CharacterStats(
            hit_points=self.hit_points,
            attack=self.attack,
            defense=self.defense,
            speed=self.speed,
            crit_rate=self.crit_rate,
            crit_damage=self.crit_damage,
            break_effect=base_character._base_stats.break_effect,
            outgoing_healing_boost=(
                base_character._base_stats.outgoing_healing_boost
            ),
            energy_regeneration_rate=(
                base_character._base_stats.energy_regeneration_rate
            ),
            effect_hit_rate=base_character._base_stats.effect_hit_rate,
            effect_res=base_character._base_stats.effect_res,
            damage_boost=base_character._base_stats.damage_boost
        )

        self._current_stats = deepcopy(self._character_stats)

    def __eq__(self, other: 'Character') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {Character} -- Character to be compared

        Returns:
            bool -- if the Characters are equal or not
        """
        if isinstance(other, Character):
            return self._base_character == other._base_character

        return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the BaseCharacter
        """
        return hash((self._base_character))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the BaseCharacter
        """
        return f'{self._base_character.name}'

    @property
    def hit_points(self) -> float:
        """Getter that calculates the hit_points parameter.

        Returns:
            float -- the hit_points parameter
        """
        hit_points = self._base_character.hit_points
        traces_stats = self._base_character.traces_stats

        return hit_points * (1 + traces_stats.hit_points / 100)

    @property
    def attack(self) -> float:
        """Getter that calculates the attack parameter.

        Returns:
            float -- the attack parameter
        """
        attack = self._base_character.attack
        traces_stats = self._base_character.traces_stats

        return attack * (1 + traces_stats.attack / 100)

    @property
    def defense(self) -> float:
        """Getter that calculates the defense parameter.

        Returns:
            float -- the defense parameter
        """
        defense = self._base_character.defense
        traces_stats = self._base_character.traces_stats

        return defense * (1 + traces_stats.defense / 100)

    @property
    def speed(self) -> float:
        """Getter that calculates the speed parameter.

        Returns:
            float -- the speed parameter
        """
        speed = self._base_character.speed
        traces_stats = self._base_character.traces_stats

        return speed + traces_stats.speed

    @property
    def crit_rate(self) -> float:
        """Getter that calculates the crit_rate parameter.

        Returns:
            float -- the crit_rate parameter
        """
        crit_rate = self._base_character.crit_rate
        traces_stats = self._base_character.traces_stats

        return crit_rate + traces_stats.crit_rate

    @property
    def crit_damage(self) -> float:
        """Getter that calculates the crit_damage parameter.

        Returns:
            float -- the crit_damage parameter
        """
        crit_damage = self._base_character.crit_damage
        traces_stats = self._base_character.traces_stats

        return crit_damage + traces_stats.crit_damage

    @property
    def current_hit_points(self) -> float:
        """Getter for the current_stats.hit_points parameter.

        Returns:
            float -- the hit_points parameter
        """
        return self._current_stats.hit_points

    @property
    def current_attack(self) -> float:
        """Getter for the current_stats.attack parameter.

        Returns:
            float -- the attack parameter
        """
        return self._current_stats.attack

    @property
    def current_defense(self) -> float:
        """Getter for the current_stats.defense parameter.

        Returns:
            float -- the defense parameter
        """
        return self._current_stats.defense

    @property
    def current_speed(self) -> float:
        """Getter for the current_stats.speed parameter.

        Returns:
            float -- the speed parameter
        """
        return self._current_stats.speed

    @property
    def current_crit_rate(self) -> float:
        """Getter for the current_stats.crit_rate parameter.

        Returns:
            float -- the crit_rate parameter
        """
        return self._current_stats.crit_rate

    @property
    def current_crit_damage(self) -> float:
        """Getter for the current_stats.crit_damage parameter.

        Returns:
            float -- the crit_damage parameter
        """
        return self._current_stats.crit_damage
