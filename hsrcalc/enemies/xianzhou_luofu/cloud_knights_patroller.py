"""This module holds the Enemy model for Cloud Knights Patroller.
"""

from ..models import EnemyTier, EnemyDamageResistences, \
    EnemyDebuffResistences, Enemy
from ...terminology import Element


class CloudKnightsPatrollerEnemy(Enemy):
    """This class holds information regarding the Cloud Knights Patroller
    Enemy.
    """

    def __init__(self):
        """CloudKnightsPatrollerEnemy constructor.
        """
        super().__init__(
            name='Cloud Knights Patroller',
            tier=EnemyTier.NORMAL,
            damage_type=Element.WIND,
            weaknesses=[Element.FIRE, Element.WIND, Element.IMAGINARY],
            toughness=60,
            hit_points=22024.0,
            attack=552.0,
            defense=1000.0,
            speed=144.0,
            effect_hit_rate=24.0,
            effect_res=20.0,
            damage_res=EnemyDamageResistences(
                physical=20.0, ice=20.0, lightning=20.0, quantum=20.0
            ),
            debuff_res=EnemyDebuffResistences()
        )
