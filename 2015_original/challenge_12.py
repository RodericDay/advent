import re, json

text = open('challenge_12.txt').read()

def explore(collection):
    # map ("object")
    if type(collection)==dict:
        if any('red' in [k, v] for k, v in collection.items()): return 0
        return sum(explore(v) for k, v in collection.items())

    # list
    elif type(collection)==list:
        return sum(explore(item) for item in collection)

    # item
    else:
        try:
            return int(collection)
        except ValueError:
            return 0

obj = json.loads(text)
print(explore(obj))
