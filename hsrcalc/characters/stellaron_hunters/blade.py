"""This module holds the character model for Blade.
"""

from ..models import CharacterStats, BaseCharacter
from ... import terminology


class BladeCharacter(BaseCharacter):
    """This class holds information regarding the Blade character.

    Extends:
        BaseCharacter
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
            traces_stats=CharacterStats(
                hit_points=28.0, crit_rate=12.0, effect_res=10.0
            )
        )
