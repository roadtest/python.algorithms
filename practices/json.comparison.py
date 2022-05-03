#!/usr/bin/env python3
def ordered(obj):
    if isinstance(obj, dict):
        print(sorted((k, ordered(v)) for k, v in obj.items()))
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj

import json

a = json.loads("""
{
    "errors": [
        {"error": "invalid", "field": "email"},
        {"error": "required", "field": "name"}
    ],
    "success": false
}
""")

b = json.loads("""
{
    "success": false,
    "errors": [
        {"error": "required", "field": "name"},
        {"error": "invalid", "field": "email"}
    ]
}
""")

print(ordered(a) == ordered(b))
