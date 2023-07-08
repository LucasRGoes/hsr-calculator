"""Unit tests of the light_cones module's classes.
"""

import unittest

from hsrcalc.terminology import Path
from hsrcalc.light_cones import BaseLightCone, LightCone, CureAndRepair


class TestLightCone(unittest.TestCase):
    """Set of unit tests for the application's Light Cone classes.
    """

    @classmethod
    def setUpClass(cls):
        """Instantiates LightCone for usage on tests.
        """
        base_light_cone = BaseLightCone(
            name='Shared Feeling',
            icon=None,
            rarity=4,
            path=Path.ABUNDANCE,
            hit_points=952,
            attack=423,
            defense=396,
            passive=CureAndRepair(),
            simulated_universe=False
        )

        cls.light_cone_1 = LightCone(
            base_light_cone=base_light_cone,
            current_level=1,
            ceiling_level=20,
            superimposition=5
        )

        cls.light_cone_2 = LightCone(
            base_light_cone=base_light_cone,
            current_level=80,
            ceiling_level=80,
            superimposition=1
        )

    def test_01(self):
        x, y, z = self.light_cone_1.hit_points
        print()
        print()
        print(x, y, z)
        print(x + y + z)
        print()


if __name__ == '__main__':
    unittest.main()
