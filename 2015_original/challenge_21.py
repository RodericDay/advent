import re, copy
import itertools as it
import collections as cl

text = open('challenge_21.txt').read()

boss = cl.Counter({
    "Hit Points": 109,
    "Damage": 8,
    "Armor": 2
})
player = cl.Counter({
    "Hit Points": 100,
    "Damage": 0,
    "Armor": 0
})

items = cl.defaultdict(list)
for line in re.findall(r'(\w+)\s+(\d+)\s+(\d+)\s+(\d+)',
    '''
    Weapon   8     4       0
    Weapon  10     5       0
    Weapon  25     6       0
    Weapon  40     7       0
    Weapon  74     8       0

    Armor   13     0       1
    Armor   31     0       2
    Armor   53     0       3
    Armor   75     0       4
    Armor  102     0       5

    Ring    25     1       0
    Ring    50     2       0
    Ring   100     3       0
    Ring    20     0       1
    Ring    40     0       2
    Ring    80     0       3
    '''):
    items[line[0]].append(dict(zip(["Cost", "Damage", "Armor"], map(int, line[1:]))))

def play_out(player, boss):
    attacker = it.cycle([player, boss])
    defender = it.cycle([boss, player])
    while True:
        a, d = next(attacker), next(defender)
        d["Hit Points"] -= max(a["Damage"] - d["Armor"], 1)
        if d["Hit Points"] <= 0:
            return a

winners = set()
losers = set()
for combo in it.product(items['Weapon'],
                        [{}]+items['Armor'],
                        [{}]+items['Ring'],
                        [{}]+items['Ring'],
                        ):
    if any(v > 1 for v in cl.Counter(map(id, combo)).values()): continue
    equipped_player = sum(map(cl.Counter, combo), player)

    if not play_out(equipped_player, cl.Counter(boss)) is not equipped_player:
        winners.add(equipped_player["Cost"])
    else:
        losers.add(equipped_player["Cost"])

print(min(winners))
print(max(losers))
