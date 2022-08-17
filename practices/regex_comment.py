#!/usr/bin/env python3

import re


def look_for(pat, str):
    return (
        "not found"
        if re.search(pat, str, flags=re.X) is None
        else re.findall(pat, str, flags=re.X)
    )


def test_always_passes():
    msg = "123:kingname456, RRR"
    pattern = r"""
    :#start
    (.*?)#match all
    ,#ending
    """
    assert look_for(pattern, msg) == ["kingname456"]


def test_fails():
    pat = r"<.+?>"
    pat1 = r"<.+>"
    msg = "<h1>hello</h1>"
    print(look_for(pat1, msg))
    assert look_for(pat1, msg) != ["<h1>"]


# print(re.findall(pattern, msg, flags=re.X))

pat = r"beat(s|ed|en|ing)"
print(look_for(pat, "beating"))

pat = r"(beat(?:s|ed|en|ing))"
print(look_for(pat, "beating"))
