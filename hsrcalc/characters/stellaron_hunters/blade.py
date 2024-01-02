"""This module holds the character model for Blade.
"""

from .. import models
from ... import terminology


class BladeCharacter(models.BaseCharacter):
    """This class holds information regarding the Blade character.

    Extends:
        models.BaseCharacter
    """

    def __init__(self):
        """BladeCharacter constructor.
        """
        super().__init__(
            name='Blade',
            rarity=terminology.Rarity.FIVE_STARS,
            path=terminology.Path.DESTRUCTION,
            combat_type=terminology.Element.WIND,
            hit_points=1358.0,
            attack=543.0,
            defense=485.0,
            speed=97.0,
            max_energy=130,
            traces_stats=models.CharacterStats(
                hit_points=28.0, crit_rate=12.0, effect_res=10.0
            )
        )

    def basic_attack(
        self,
        enhanced: models.AbilityEnhancement = models.AbilityEnhancement.TIER_I
    ) -> models.CharacterAbility:
        """The character's basic attack description should be returned.

        Arguments:
            enhanced {models.AbilityEnhancement} -- if the returned ability
            should be the enhanced one or not

        Returns:
            models.CharacterAbility -- the description for the ability
        """
        if enhanced == models.AbilityEnhancement.TIER_I:
            return models.CharacterAbility(
                name='Shard Sword',
                type_=models.AbilityType.BASIC_ATK,
                class_=models.AbilityClass.SINGLE_TARGET,
                damage_calculation={'attack': [1]},
                damage_distribution=[0.5, 0.5],
                energy_generation=20,
                toughness=[30]
            )

        return models.CharacterAbility(
            name='Forest of Swords',
            type_=models.AbilityType.BASIC_ATK,
            class_=models.AbilityClass.BLAST,
            damage_calculation={'hit_points': [1, 0.4], 'attack': [0.4, 0.16]},
            damage_distribution=[0.5, 0.5],
            energy_generation=30,
            toughness=[60, 30]
        )
