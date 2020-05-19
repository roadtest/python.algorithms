#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse(text):
    res = []
    for item in text.split(','):
        res.append(int(item))
    return res

print(parse("1,2,3"))
