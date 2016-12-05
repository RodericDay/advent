import re, collections, types


class Game:

    class WinEvent(RuntimeError): pass
    class LoseEvent(RuntimeError): pass
    class InvalidEvent(RuntimeError): pass

    def __init__(self, player_hp, player_mp, enemy_hp, enemy_atk,
                 effect_stack=None, spell_history=None):
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.effect_stack = effect_stack or tuple()
        self.spell_history = spell_history or tuple()

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        try:
            if self.enemy_hp < 1: raise Game.WinEvent
            if self.player_hp < 1: raise Game.LoseEvent
            if self.player_mp < 0: raise Game.InvalidEvent
        except AttributeError:
            pass

    @property
    def is_player_turn(self):
        return len(self.spell_history)%2==0

    @property
    def total_mana_spent(self):
        return sum(spell_book[spell].cost for spell in self.spell_history if spell)

    def consume_effect_stack(self):
        counter = collections.Counter(self.effect_stack)
        active = set(counter.elements())
        counter -= {k:1 for k in active}
        self.effect_stack = tuple(counter.elements())
        return active

    def copy(self):
        return Game(**self.__dict__)

    def __str__(self):
        inner = ", ".join("{}={}".format(k, getattr(self, k))
            for k in ["player_hp", "enemy_hp"])
        return "Game({})".format(inner)


Spell = collections.namedtuple("Spell", "cost duration")
spell_book = {
    "Magic Missile": Spell(53, 0),
    "Drain": Spell(73, 0),
    "Shield": Spell(113, 6),
    "Poison": Spell(173, 6),
    "Recharge": Spell(229, 5),
}


def resolve(spell_cast, state, hard_mode=False):
    state = state.copy()

    if state.is_player_turn and hard_mode: state.player_hp -= 1

    active = state.consume_effect_stack()
    player_def = 7 if 'Shield' in active else 0
    state.player_mp += 101 if 'Recharge' in active else 0
    state.enemy_hp -= 3 if 'Poison' in active else 0

    if state.is_player_turn:
        if spell_cast in state.effect_stack: raise Game.InvalidEvent
        state.player_mp -= spell_book[spell_cast].cost
        state.effect_stack += (spell_cast,) * spell_book[spell_cast].duration
        if spell_cast == 'Magic Missile': state.enemy_hp -= 4
        if spell_cast == 'Drain': state.enemy_hp -= 2; state.player_hp += 2

    else:
        state.player_hp -= max(1, state.enemy_atk-player_def)

    state.spell_history += (spell_cast,)
    return state

def check_sequence(state, sequence):
    try:
        for spell in (action for spell in sequence for action in [spell, None]):
            state = resolve(spell, state)
    except Game.WinEvent:
        return True

assert check_sequence(Game(10, 250, 13, 8), ['Poison', 'Magic Missile'])
assert check_sequence(Game(10, 250, 14, 8), ['Recharge','Shield','Drain','Poison','Magic Missile'])


win_states = []
def breadth_first_search(valid_states):
    ''' consider only valid branches, keep track of successful ones '''
    for state in valid_states:
        for spell in (spell_book if state.is_player_turn else [None]):
            try:
                yield resolve(spell, state, hard_mode=True)
            except Game.WinEvent:
                end_state = state.copy()
                end_state.spell_history += (spell,)
                win_states.append(end_state)
            except (Game.LoseEvent, Game.InvalidEvent):
                pass


ongoing_states = [Game(50, 500, 51, 9)]
for n in range(16):  # how many turns in
    ongoing_states = list(breadth_first_search(ongoing_states))


ans = min(state.total_mana_spent for state in win_states)
print(ans)
