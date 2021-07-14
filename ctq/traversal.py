"""A slection of choice methods to help navigate around a resource tree
"""

from typing import Any
from typing import Iterable


def traverse_up(obj: Any) -> Iterable[Any]:
    """Returns: An iteratable starting with the object, then it's parent, grand
    parent, etc.  until the iterator reaches a point where there is no more
    ancestors.
    """
    current = obj
    while current is not None:
        yield current
        current = getattr(current, "__parent__", None)


def get_root(obj: Any) -> Any:
    """Returns: the object that it at the root of a resource tree."""
    lineage = list(traverse_up(obj))
    return lineage[-1]


def resource_path_names(obj: Any) -> tuple[str]:
    """Returns: A tuple of path names from the root object to the ``obj``"""
    names = []
    for resource in traverse_up(obj):
        name = getattr(resource, "__name__", None)
        if name is None:  # It is not possible to calculate the resource path names
            return None
        names.append(name)
    names.reverse()
    return tuple(names)
