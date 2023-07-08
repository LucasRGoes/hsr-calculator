"""Implements the Light Cone passive ability "Morn, Noon, Dusk and Night"'s
logic.
"""

from ...models import PassiveLightCone


def MornNoonDuskAndNight(PassiveLightCone):
	"""The class for the Light Cone passive ability "Morn, Noon, Dusk and
    Night".

	Extends:
		PassiveLightCone
	"""

    @property
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        return 'Morn, Noon, Dusk and Night'

    @property
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        return ("Increases the wearer's Max HP by 18-30\% and Outgoing "
                "Healing by 12-20\%. When the wearer heals allies, record the "
                "amount of Outgoing Healing. When any ally launches an "
                "attack, a random attacked enemy takes additional DMG equal "
                "to 36-60\% of the recorded Outgoing Healing value. This "
                "Additional DMG is of the same Type as the wearer's, is not "
                "affected by other buffs, and can only occur 1 time per turn.")

    @property
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        return [
            (18, 12, 36),   # Superimposition I
            (21, 14, 42),   # Superimposition II
            (24, 16, 48),   # Superimposition III
            (27, 18, 54),   # Superimposition IV
            (30, 20, 60)    # Superimposition V
        ]

    def apply(self):
        """This method implements the Light Cone passive ability's buffs or
        debuffs.
        """
        pass
