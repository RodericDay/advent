import json


def recurse(data, avoid=None):
    type_ = type(data)
    if type_ is int:
        return data
    elif type_ is str:
        return 0
    elif type_ is list:
        return sum(recurse(el, avoid) for el in data)
    elif type_ is dict:
        if any(val == avoid for val in data.values()): return 0
        return sum(recurse(value, avoid) for key, value in data.items())


data = json.loads(df.read_text())
ans1 = recurse(data)
ans2 = recurse(data, 'red')
