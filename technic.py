from enum import Enum
from functools import wraps
from typing import Callable


class TechicType(Enum):
    EXPENSIVE = "expensive"
    CHEAP = "cheap"


EXPENSIVE_COST = 500


def compare_technic_by_name(obj: Callable) -> Callable:
    @wraps(obj, updated=())
    class Comparator(obj):
        __slots__ = ()

        def __init__(self, *args, **kwargs):
            super(Comparator, self).__init__(*args, **kwargs)

        def __eq__(self, other):
            if issubclass(type(other), Comparator):
                return len(self.name) == len(other.name)
            raise TypeError

        def __lt__(self, other):
            if issubclass(type(other), Comparator):
                return len(self.name) < len(other.name)
            raise TypeError

    return Comparator


@compare_technic_by_name
class Technic:
    __slots__ = (
        "name",
        "cost",
        "is_available",
        "type"
    )

    def __init__(self, name: str, cost: float, is_available: bool):
        self.name = name
        self.cost = cost
        self.is_available = is_available
        self.type = TechicType.EXPENSIVE.value \
            if self.cost >= EXPENSIVE_COST \
            else TechicType.CHEAP.value


# Solution with dunder methods
#
# class Technic:
#     __slots__ = (
#         "name",
#         "cost",
#         "is_available",
#         "type"
#     )
#
#     def __init__(self, name: str, cost: float, is_available: bool):
#         self.name = name
#         self.cost = cost
#         self.is_available = is_available
#         self.type = TechicType.EXPENSIVE.value \
#             if self.cost >= EXPENSIVE_COST \
#             else TechicType.CHEAP.value
#
#     def __eq__(self, other):
#         if isinstance(other, Technic):
#             return len(self.name) == len(other.name)
#         raise TypeError
#
#     def __lt__(self, other):
#         if isinstance(other, Technic):
#             return len(self.name) < len(other.name)
#         raise TypeError


if __name__ == '__main__':
    t1 = Technic("Computer", 120, True)
    t2 = Technic("Computer", 170, True)
    t3 = Technic("Very-very good computer", 530, False)

    assert t1.type == "cheap"
    assert t3.type == "expensive"
    assert t1 == t2
    assert t1 < t3
    assert t3 > t2
