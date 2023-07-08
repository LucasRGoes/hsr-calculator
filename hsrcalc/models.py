"""These are the models of the application. They hold important data and
methods concerning stats data.
"""

from .enums import *


class BaseLightCone(object):
    """The BaseLightCone class holds stats and other information regarding\
    HSR's light cones.
    """

    def __init__(
        self,
        name: str,
        icon: str,
        rarity: int,
        path: Path,
        hit_points: float,
        attack: float,
        defense: float,
        passive_name: str,
        passive_description: str,
        simulated_universe: bool
    ):
        """BaseLightCone constructor.

        Arguments:
            name {str} -- the Light Cone's name
            icon {str} -- the Light Cone's icon
            rarity {int} -- the Light Cone's rarity, ranging from 3* to 5*
            path {Path} -- the Light Cone's path
            hit_points {float} -- the Light Cone's Hit Points or HP for short
            attack {float} -- the Light Cone's Attack or ATK for short
            defense {float} -- the Light Cone's Defense, or DEF for short
            passive_name {str} -- the Light Cone's passive ability's name
            passive_description {str} -- the Light Cone's passive ability
            description
            simulated_universe {bool} -- if the Light Cone is obtained through
            the Simulated Universe's shop
        """
        self._name = name
        self._icon = icon
        self._rarity = rarity
        self._path = path
        self._hit_points = hit_points
        self._attack = attack
        self._defense = defense
        self._passive_name = passive_name
        self._passive_description = passive_description
        self._simulated_universe = simulated_universe

    def __eq__(self, other: 'BaseLightCone') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {BaseLightCone} -- Light Cone to be compared

        Returns:
            bool -- if the Light Cones are equal or not
        """
        if type(other) == BaseLightCone:
            return self.name == other.name \
                and self.icon == other.icon \
                and self.rarity == other.rarity \
                and self.path == other.path \
                and self.hit_points == other.hit_points \
                and self.attack == other.attack \
                and self.defense == other.defense \
                and self.passive_name == other.passive_name \
                and self.passive_description == other.passive_description \
                and self.simulated_universe == other.simulated_universe

        else:
            return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the Light Cone
        """
        return hash((
            self.name,
            self.icon,
            self.rarity,
            self.path,
            self.hit_points,
            self.attack,
            self.defense,
            self.passive_name,
            self.passive_description,
            self.simulated_universe
        ))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Light Cone
        """
        return f'{self.name} ({self.rarity}*) - The {self.path_as_str}'

    @property
    def name(self) -> str:
        return self._name

    @property
    def icon(self) -> str:
        return self._icon

    @property
    def encoded_icon(self) -> bytes:
        return self._icon.encode('utf-8')

    @property
    def rarity(self) -> int:
        return self._rarity

    @property
    def path(self) -> Path:
        return self._path

    @property
    def path_as_str(self) -> str:
        return self._path.name.capitalize()

    @property
    def path_as_int(self) -> int:
        return self._path.value

    @property
    def hit_points(self) -> float:
        return self._hit_points

    @property
    def attack(self) -> float:
        return self._attack

    @property
    def defense(self) -> float:
        return self._defense

    @property
    def hp(self) -> float:
        return self._hit_points

    @property
    def atk(self) -> float:
        return self._attack

    @property
    def def_(self) -> float:
        return self._defense

    @property
    def passive_name(self) -> str:
        return self._passive_name

    @property
    def passive_description(self) -> str:
        return self._passive_description

    @property
    def simulated_universe(self) -> bool:
        return self._simulated_universe
