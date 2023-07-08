"""These are the Light Cone models of the application. They hold important
data and methods concerning stats data of HSR's Light Cones.
"""

import abc

from ..terminology import *


class PassiveLightCone(abc.ABC):
    """The PassiveLightCone class holds basic information regarding HSR's
    Light Cones's passive abilities.

    Extends:
        abc.ABC
    """

    def __init__(self):
        """PassiveLightCone's constructor.
        """
        pass

    def __eq__(self, other: 'PassiveLightCone') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {PassiveLightCone} -- Light Cone passive ability to be
            compared

        Returns:
            bool -- if the Light Cone passive ability is equal or not
        """
        if type(other) == PassiveLightCone:
            return self.name == other.name and \
                self.description == other.description

        else:
            return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the Light Cone passive ability
        """
        return hash((self.name, self.description))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the Light Cone passive ability
        """
        return f'{self.name}: {self.description}'

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Returns the Light Cone passive ability's name.

        Returns:
            str -- the name
        """
        pass

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Returns the Light Cone passive ability's description.

        Returns:
            str -- the description
        """
        pass

    @property
    @abc.abstractmethod
    def multipliers(self) -> 'list[tuple]':
        """Returns the Light Cone passive ability's multipliers.

        Returns:
            list[tuple] -- the multipliers
        """
        pass

    @abc.abstractmethod
    def apply(self):
        """This method should be used to implement the Light Cone passive
        ability's buffs or debuffs.
        """
        pass


class BaseLightCone(object):
    """The BaseLightCone class holds stats and other information regarding
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
        passive: PassiveLightCone,
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
            passive {PassiveLightCone} -- the Light Cone's passive ability
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
        self._passive = passive
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
                and self.passive == other.passive \
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
            self.passive,
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
    def passive(self) -> PassiveLightCone:
        return self._passive

    @property
    def simulated_universe(self) -> bool:
        return self._simulated_universe


class LightCone(object):
    """The LightCone class holds stats and other information regarding
    HSR's built light cones.
    """

    def __init__(
        self,
        base_light_cone: BaseLightCone,
        current_level: int,
        ceiling_level: int,
        superimposition: int
    ):
        """LightCone constructor.

        Arguments:
            base_light_cone {BaseLightCone} -- the base of this built Light
            Cone
            current_level {int} -- the built Light Cone's current level
            ceiling_level {int} -- the built Light Cone's ceiling level
            superimposition {int} -- the built Light Cone's superimposition
            level
        """
        self._base_light_cone = base_light_cone
        self._current_level = current_level
        self._ceiling_level = ceiling_level
        self._superimposition = superimposition

    def __eq__(self, other: 'LightCone') -> bool:
        """Equality operator's magic method.

        Arguments:
            other {LightCone} -- built Light Cone to be compared

        Returns:
            bool -- if the built Light Cones are equal or not
        """
        if type(other) == LightCone:
            return self.base_light_cone == other.base_light_cone \
                and self.current_level == other.current_level \
                and self.ceiling_level == other.ceiling_level \
                and self.superimposition == other.superimposition

        else:
            return False

    def __hash__(self) -> int:
        """Hash operator's magic method.

        Returns:
            int -- the hash value of the built Light Cone
        """
        return hash((
            self.base_light_cone,
            self.current_level,
            self.ceiling_level,
            self.superimposition
        ))

    def __str__(self) -> str:
        """String operator's magic method.

        Returns:
            str -- string representation of the built Light Cone
        """
        return (f'{self.base_light_cone}: Lvl. '
                f'{self.current_level}/{self.ceiling_level} '
                f'(Superimposition {self.superimposition_as_str})')

    @property
    def base_light_cone(self) -> BaseLightCone:
        return self._base_light_cone

    @property
    def current_level(self) -> int:
        return self._current_level

    @property
    def ceiling_level(self) -> int:
        return self._ceiling_level

    @property
    def superimposition(self) -> int:
        return self._superimposition

    @property
    def superimposition_as_str(self) -> str:
        if self.superimposition == 1:
            return 'I'
        elif self.superimposition == 2:
            return 'II'
        elif self.superimposition == 3:
            return 'III'
        elif self.superimposition == 4:
            return 'IV'
        elif self.superimposition == 5:
            return 'V'

    @property
    def hit_points(self) -> float:
        x = self.base_light_cone.hp / 4.8
        y = self.base_light_cone.atk / 2.4
        z = self.base_light_cone.def_ / 3

        return x, y, z

        if self.base_light_cone.rarity == 3:
            pass

        elif self.base_light_cone.rarity == 4:
            pass

        elif self.base_light_cone.rarity == 5 \
                and self.base_light_cone.simulated_universe is False:
            pass

        elif self.base_light_cone.rarity == 5 \
                and self.base_light_cone.simulated_universe is True:
            pass

    # @property
    # def attack(self) -> float:
    #     return self._attack

    # @property
    # def defense(self) -> float:
    #     return self._defense
