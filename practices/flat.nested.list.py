#!/usr/bin/env python3
from typing import List, Any, Iterable


def flatten(inputList: List[Any]) -> Iterable[Any]:
    """
    Flatten a list using generators comprehensions.
        Returns a flattened version of list lst.
    """

    for sublist in inputList:
        if isinstance(sublist, list):

            # for item in sublist:
            #    yield item
            yield from flatten(sublist)
        else:
            yield sublist


lst = [["hello", "world"], ["my", "dear"], "friend", 1, 3.4, 5, 69.9, [["a", "b"]]]

print(list(flatten(lst)))
