"""This module holds the classes used for calculation purposes.
"""

import random
from copy import deepcopy

from . import characters, enemies


class Character:
    """The Character class is used to describe a character fully equipped and
    on a battle situation.
    """

    def __init__(self, base_character: characters.BaseCharacter):
        """Character constructor.

        Arguments:
            base_character {characters.BaseCharacter} -- The base character
        """
        self._base_character = base_character

        self._character_stats = characters.CharacterStats(
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
            int -- the hash value of the Character
        """
        return hash((self._base_character))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Character
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

    def basic_attack(self, target: object):
        """The character's basic attack should be applied to a chosen target.

        Arguments:
            target {object} -- the target to have the basic attack applied to
        """
        ability = self._base_character.basic_attack()

        # Calculating base damage
        base_damage = 0
        for stat, percentage in ability.damage_calculation.items():
            if stat == 'hit_points':
                current_stat = self.hit_points
            elif stat == 'attack':
                current_stat = self.current_attack
            else:
                current_stat = self.current_attack

            base_damage += current_stat * percentage[0]

        # Calculating crit multiplier
        if random.random() < (self.current_crit_rate / 100):
            crit_multiplier = 1 + self.current_crit_damage / 100
        else:
            crit_multiplier = 1

        # Calculating damage boost multipler
        damage_boost_multiplier = 1 + self._character_stats.damage_boost

        # Calculating defense multiplier
        defense_multiplier = 1 - (
            target.current_defense / (target.current_defense + 280)
        )

        return (
            base_damage
            * crit_multiplier
            * damage_boost_multiplier
            * defense_multiplier
        )


class Enemy:
    """The Enemy class is used to describe an enemy on a battle situation.
    """

    def __init__(self, base_enemy: enemies.BaseEnemy):
        """Enemy constructor.

        Arguments:
            base_enemy {enemies.BaseEnemy} -- The base enemy
        """
        self._base_enemy = base_enemy

        self._enemy_stats = deepcopy(base_enemy._base_stats)
        self._current_stats = deepcopy(self._enemy_stats)

    def __eq__(self, other: 'Enemy') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {Enemy} -- Enemy to be compared

        Returns:
            bool -- if the Characters are equal or not
        """
        if isinstance(other, Enemy):
            return self._base_enemy == other._base_enemy

        return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the Enemy
        """
        return hash((self._base_enemy))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Enemy
        """
        return f'{self._base_enemy.name}'

    @property
    def hit_points(self) -> float:
        """Getter for the hit_points parameter.

        Returns:
            float -- the hit_points parameter
        """
        return self._enemy_stats.hit_points

    @property
    def attack(self) -> float:
        """Getter for the attack parameter.

        Returns:
            float -- the attack parameter
        """
        return self._enemy_stats.attack

    @property
    def defense(self) -> float:
        """Getter for the defense parameter.

        Returns:
            float -- the defense parameter
        """
        return self._enemy_stats.defense

    @property
    def speed(self) -> float:
        """Getter for the speed parameter.

        Returns:
            float -- the speed parameter
        """
        return self._enemy_stats.speed

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
