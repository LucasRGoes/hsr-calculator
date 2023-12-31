"""This module holds the Character model for Blade.
"""

from ..models import CharacterStats, Character
from ...terminology import Element, Path, Rarity


class BladeCharacter(Character):
    """This class holds information regarding the Blade Character.
    """

    def __init__(self):
        """BladeCharacter constructor.
        """
        super().__init__(
            name='Blade',
            rarity=Rarity.FIVE_STARS,
            path=Path.DESTRUCTION,
            combat_type=Element.WIND,
            hit_points=1358.0,
            attack=543.0,
            defense=485.0,
            speed=97.0,
            max_energy=130,
            traces_stats=CharacterStats(
                hit_points=28.0, crit_rate=12.0, effect_res=10.0
            )
        )
