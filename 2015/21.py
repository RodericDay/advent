import re, itertools

win, loss = True, False
def resolve(atk, arm):
    player_hp = 100
    enemy_hp = 109
    enemy_atk = 8
    enemy_def = 2
    while True:
        enemy_hp -= (atk-enemy_def)
        if enemy_hp < 0: return win
        player_hp -= (enemy_atk-arm)
        if player_hp < 0: return loss

def parse_item_string(string):
    return [tuple(int(s) for s in re.findall(r'\s\d+', line))
        for line in string.strip().split('\n')]

nothing = (0,0,0)

weapons = parse_item_string('''
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
''')

armors = [nothing] + parse_item_string('''
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
''')

rings = [nothing, nothing] + parse_item_string('''
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
''')

tally = {win: [], loss: []}
for items in itertools.product(weapons, armors, rings, rings):
    cost, atk, arm = map(sum, zip(*set(items)))
    tally[resolve(atk, arm)].append(cost)

print(min(tally[win]))
print(max(tally[loss]))
