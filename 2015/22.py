import re, collections, types

class GameState:

    def __init__(self, player_hp, player_mp, enemy_hp, enemy_atk, ongoing):
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.ongoing = ongoing

    def copy(self):
        return GameState(**self.__dict__)

    def __str__(self):
        inner = ", ".join("{}={}".format(k, getattr(self, k))
            for k in ["player_hp", "enemy_hp"])
        return "GameState({})".format(inner)


Spell = collections.namedtuple("Spell", "cost duration")
spell_book = {
    "Magic Missile": Spell(53, 0),
    "Drain": Spell(73, 0),
    "Shield": Spell(113, 6),
    "Poison": Spell(173, 6),
    "Recharge": Spell(229, 5),
}


def resolve(spell_cast, state, hard=False):
    state = state.copy()
    player_turn = spell_cast is not None

    if hard and player_turn:
        state.player_hp -= 1
        if state.player_hp < 1: return "loss", None

    # resolve ongoing effects
    ongoing_spells = collections.Counter(state.ongoing)
    active = set(ongoing_spells.elements())
    ongoing_spells -= {k:1 for k in active}  # decrease cooldown
    player_def = 7 if 'Shield' in active else 0
    state.player_mp += 101 if 'Recharge' in active else 0
    state.enemy_hp -= 3 if 'Poison' in active else 0
    if state.enemy_hp < 1: return "win", None

    if player_turn:
        # casting an active spell is invalid
        if spell_cast in ongoing_spells.elements(): return "invalid", None
        # casting a spell without required mp is invalid
        state.player_mp -= spell_book[spell_cast].cost
        if state.player_mp < 0: return "invalid", None
        # assign cooldown
        ongoing_spells[spell_cast] = spell_book[spell_cast].duration
        # handle instantaneous spells
        if spell_cast == 'Magic Missile': state.enemy_hp -= 4
        if spell_cast == 'Drain': state.enemy_hp -= 2; state.player_hp += 2
        # win condition
        if state.enemy_hp < 1: return "win", None

    else:
        state.player_hp -= max(1, state.enemy_atk-player_def)
        if state.player_hp < 1: return "loss", None

    # state transfer
    state.ongoing = tuple(ongoing_spells.elements())
    return "ongoing", state

def resolve_sequence(state, sequence):
    for spell in (action for spell in sequence for action in [spell, None]):
        status, state = resolve(spell, state)
    return status

assert resolve_sequence(GameState(10, 250, 13, 8, None), ['Poison', 'Magic Missile']) == 'win'
assert resolve_sequence(GameState(10, 250, 14, 8, None), ['Recharge','Shield','Drain','Poison','Magic Missile']) == "win"

def breadth_first_search(valid_states, successful_sequences):
    ''' consider only valid branches, keep track of successful ones '''
    ongoing_states = []
    for history, state in valid_states:
        for spell in (spell_book if len(history)%2==0 else [None]):
            new_history = history + [spell]
            status, new_state = resolve(spell, state, hard=True)
            if status=='ongoing':
                ongoing_states.append((new_history, new_state))
            if status=='win':
                successful_sequences.append(new_history)
    return ongoing_states

ongoing_states = [([],GameState(50, 500, 51, 9, None))]
successful_sequences = []
for n in range(16):
    ongoing_states = breadth_first_search(ongoing_states, successful_sequences)

ans = 9999
for timeline in successful_sequences:
    cost = sum(spell_book[spell].cost for spell in timeline if spell)
    if cost and cost <= ans:
        ans = cost
print(ans)
