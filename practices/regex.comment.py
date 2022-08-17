#!/usr/bin/env python3

import re

msg = "123:kingname456, RRR"
pattern = r"""
:#start
(.*?)#match all
,#ending
"""
print(re.findall(pattern, msg, flags=re.X))
