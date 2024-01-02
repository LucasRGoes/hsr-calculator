"""This module holds the Enemy model for Cloud Knights Patroller.
"""

from .. import models
from ... import terminology


class CloudKnightsPatrollerEnemy(models.BaseEnemy):
    """This class holds information regarding the Cloud Knights Patroller
    Enemy.

    Extends:
        models.BaseEnemy
    """

    def __init__(self):
        """CloudKnightsPatrollerEnemy constructor.
        """
        super().__init__(
            name='Cloud Knights Patroller',
            tier=models.EnemyTier.NORMAL,
            damage_type=terminology.Element.WIND,
            weaknesses=[
                terminology.Element.FIRE,
                terminology.Element.WIND,
                terminology.Element.IMAGINARY
            ],
            toughness=60,
            hit_points=22024.0,
            attack=552.0,
            defense=1000.0,
            speed=144.0,
            effect_hit_rate=24.0,
            effect_res=20.0,
            damage_res=models.EnemyDamageResistences(
                physical=20.0, ice=20.0, lightning=20.0, quantum=20.0
            ),
            debuff_res=models.EnemyDebuffResistences()
        )
