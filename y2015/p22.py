from collections import namedtuple
import itertools


def play(spell, state):
    is_win = 0
    hp, mp, boss_hp, boss_dmg, turns, mp_spent, is_hard = state
    for turn in (spell, None):
        # prelude
        if turn is not None and is_hard:
            hp -= 1
            if hp <= 0:
                is_win = -1
                break
        if 'r' in turns[-5:]:
            mp += 101
        if 'p' in turns[-6:]:
            boss_hp -= 3
            if boss_hp <= 0:
                is_win = 1
                break
        # action
        if turn == 'm':
            mp_spent += 53
            boss_hp -= 4
        elif turn == 'd':
            mp_spent += 73
            boss_hp -= 2
            hp += 2
        elif turn == 's':
            mp_spent += 113
            if 's' in turns[-5:]:
                is_win = -1
                break
        elif turn == 'p':
            mp_spent += 173
            if 'p' in turns[-5:]:
                is_win = -1
                break
        elif turn == 'r':
            mp_spent += 229
            if 'r' in turns[-4:]:
                is_win = -1
                break
        elif turn == None:
            hp -= max(boss_dmg - 7 if 's' in turns[-6:] else boss_dmg, 1)
        turns += (turn,)
        # denouement
        if mp_spent > mp:
            is_win = -1
            break
        if boss_hp <= 0:
            is_win = 1
            break
        if hp <= 0:
            is_win = -1
            break
    return is_win, State(hp, mp, boss_hp, boss_dmg, turns, mp_spent, is_hard)


State = namedtuple('State', 'hp,mp,boss_hp,boss_dmg,turns,mp_spent,is_hard')
boss_hp, boss_dmg = map(int, re.findall(r'\d+', text))

pending, wins = [State(50, 500, boss_hp, boss_dmg, tuple(), 0, False)], set()
while not wins:
    outcomes = [play(spell, state) for state in pending for spell in 'mdspr']
    wins |= {state for is_win, state in outcomes if is_win == 1}
    pending = [state for is_win, state in outcomes if is_win == 0]
ans1 = min(win.mp_spent for win in wins)

pending, wins = [State(50, 500, boss_hp, boss_dmg, tuple(), 0, True)], set()
while not wins:
    outcomes = [play(spell, state) for state in pending for spell in 'mdspr']
    wins |= {state for is_win, state in outcomes if is_win == 1}
    pending = [state for is_win, state in outcomes if is_win == 0]
ans2 = min(win.mp_spent for win in wins)
