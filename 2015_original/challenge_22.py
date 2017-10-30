import collections as cl

def resolve(hp, mp, boss_hp, boss_atk, spell_order):
    effects = cl.defaultdict(cl.Counter)
    roll = (action for spell in spell_order for action in [spell, None])
    cum = 0
    for turn, action in enumerate(roll):

        mp += effects[turn]['mp']

        boss_hp -= effects[turn]['psn']
        if boss_hp <= 0:
            return cum

        if action is None:
            hp -= max(1, boss_atk - effects[turn]['def'])
            if hp <= 0:
                raise RuntimeError("Player died on turn {}".format(turn))

        elif action is 'R':
            cum += 229
            mp -= 229
            for n in range(turn+1, turn+1+5):
                if effects[n]['mp']:
                    raise RuntimeError("Overcast R")
                effects[n]['mp'] = 101

        elif action is 'S':
            cum += 113
            mp -= 113
            for n in range(turn+1, turn+1+6):
                if effects[n]['def']:
                    raise RuntimeError("Overcast S")
                effects[n]['def'] = 7

        elif action is 'D':
            cum += 73
            mp -= 73
            hp += 2
            boss_hp -= 2

        elif action is 'P':
            cum += 173
            mp -= 173
            for n in range(turn+1, turn+1+6):
                if effects[n]['psn']:
                    raise RuntimeError("Overcast P")
                effects[n]['psn'] = 3

        elif action is 'M':
            cum += 53
            mp -= 53
            boss_hp -= 4

        else:
            raise RuntimeError("Unkown action: {}".format(action))

        if mp <= 0:
            raise RuntimeError("Ran out of magic")

    else:
        raise RuntimeError(("Ran out of spells with {} HP and {} MP left. " + \
                           "Boss had {} HP left. Spent {} MP total.").format(hp, mp, boss_hp, cum))

print(resolve(50, 250, 51, 9, 'RS'))
