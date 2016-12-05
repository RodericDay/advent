import re, collections, types


class GameState:

    class Event(RuntimeError):
        pass

    def __init__(self, player_hp, player_mp, enemy_hp, enemy_atk, ongoing=None, spell_history=None):
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.ongoing = ongoing
        self.spell_history = spell_history or tuple()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        try:
            if self.player_hp < 1: raise GameState.Event("lose")
            if self.player_mp < 0: raise GameState.Event("invalid")
            if self.enemy_hp < 1: raise GameState.Event("win")
        except AttributeError:
            pass

    @property
    def is_player_turn(self):
        return len(self.spell_history)%2==0

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

    if hard and state.is_player_turn:
        state.player_hp -= 1

    # resolve ongoing effects
    ongoing_spells = collections.Counter(state.ongoing)
    active = set(ongoing_spells.elements())
    ongoing_spells -= {k:1 for k in active}  # decrease cooldown
    player_def = 7 if 'Shield' in active else 0
    state.player_mp += 101 if 'Recharge' in active else 0
    state.enemy_hp -= 3 if 'Poison' in active else 0

    if state.is_player_turn:
        if spell_cast in ongoing_spells.elements(): raise GameState.Event("invalid")
        state.player_mp -= spell_book[spell_cast].cost
        ongoing_spells[spell_cast] = spell_book[spell_cast].duration
        if spell_cast == 'Magic Missile': state.enemy_hp -= 4
        if spell_cast == 'Drain': state.enemy_hp -= 2; state.player_hp += 2

    else:
        state.player_hp -= max(1, state.enemy_atk-player_def)

    state.spell_history += (spell_cast,)
    state.ongoing = tuple(ongoing_spells.elements())
    return state

def resolve_sequence(state, sequence):
    try:
        for spell in (action for spell in sequence for action in [spell, None]):
            state = resolve(spell, state)
    except GameState.Event as event:
        return str(event)

assert resolve_sequence(GameState(10, 250, 13, 8), ['Poison', 'Magic Missile']) == "win"
assert resolve_sequence(GameState(10, 250, 14, 8), ['Recharge','Shield','Drain','Poison','Magic Missile']) == "win"

def breadth_first_search(valid_states, successful_sequences):
    ''' consider only valid branches, keep track of successful ones '''
    ongoing_states = []
    for state in valid_states:
        for spell in (spell_book if state.is_player_turn else [None]):

            try:
                new_state = resolve(spell, state, hard=True)
                ongoing_states.append(new_state)

            except GameState.Event as status:
                if str(status)=='win':
                    successful_sequences.append(state.spell_history+(spell,))

    return ongoing_states


ongoing_states = [GameState(50, 500, 51, 9)]
successful_sequences = []
for n in range(16):
    ongoing_states = breadth_first_search(ongoing_states, successful_sequences)


ans = 9999
for timeline in successful_sequences:
    cost = sum(spell_book[spell].cost for spell in timeline if spell)
    if cost and cost <= ans:
        ans = cost
print(ans)
