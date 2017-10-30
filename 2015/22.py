import re, collections


Spell = collections.namedtuple("Spell", "cost duration")
spell_book = {
    "Magic Missile": Spell(53, 0),
    "Drain": Spell(73, 0),
    "Shield": Spell(113, 6),
    "Poison": Spell(173, 6),
    "Recharge": Spell(229, 5),
}


class Game:

    class Event(RuntimeError):
        def __init__(self, state):
            self.state = state

    class WinEvent(Event): pass
    class LoseEvent(Event): pass
    class InvalidEvent(Event): pass

    def __init__(self, player_hp, player_mp, enemy_hp, enemy_atk, turn=1,
                 effect_stack=tuple(), spell_history=tuple(), hard_mode=False):
        self.player_hp = player_hp
        self.player_mp = player_mp
        self.enemy_hp = enemy_hp
        self.enemy_atk = enemy_atk
        self.turn = turn
        self.effect_stack = effect_stack
        self.spell_history = spell_history
        self.hard_mode = hard_mode

    def resolve_turn(self, spell):
        state = self.copy()

        if state.is_player_turn and state.hard_mode: state.player_hp -= 1

        active = state.consume_effect_stack()
        shield = 7 if 'Shield' in active else 0
        state.player_mp += 101 if 'Recharge' in active else 0
        state.enemy_hp -= 3 if 'Poison' in active else 0

        if state.is_player_turn:
            state.cast_spell(spell)  # handle generic spell stuff
            if spell == 'Magic Missile': state.enemy_hp -= 4
            if spell == 'Drain': state.enemy_hp -= 2; state.player_hp += 2

        else:
            state.player_hp -= max(1, state.enemy_atk-shield)

        state.turn += 1
        return state

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        try:
            if self.enemy_hp < 1: raise Game.WinEvent(self)
            if self.player_hp < 1: raise Game.LoseEvent(self)
            if self.player_mp < 0: raise Game.InvalidEvent(self)
        except AttributeError:
            pass

    @property
    def is_player_turn(self):
        return self.turn % 2 == 1

    @property
    def total_mana_spent(self):
        return sum(spell_book[spell].cost for spell in self.spell_history)

    def cast_spell(self, spell):
        if spell not in spell_book: raise Game.InvalidEvent(self)
        if spell in self.effect_stack: raise Game.InvalidEvent(self)
        self.player_mp -= spell_book[spell].cost
        self.effect_stack += (spell,) * spell_book[spell].duration
        self.spell_history += (spell,)

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

    def check_sequence(self, sequence):
        state = self.copy()
        try:
            for spell in sequence:
                for action in [spell, None]:
                    state = state.resolve_turn(action)
        except Game.WinEvent:
            return True


def breadth_first_search(states, lim=20):
    win_states = []
    for i in range(lim):
        states, old_states = [], states
        for state in old_states:
            for spell in (spell_book if state.is_player_turn else [None]):
                try:
                    states += [state.resolve_turn(spell)]
                except Game.WinEvent as event:
                    win_states += [event.state]
                except (Game.LoseEvent, Game.InvalidEvent):
                    pass
    return win_states


assert Game(10, 250, 13, 8).check_sequence(['Poison', 'Magic Missile'])
assert Game(10, 250, 14, 8).check_sequence(
                        ['Recharge','Shield','Drain','Poison','Magic Missile'])

win_states = breadth_first_search([Game(50, 500, 51, 9, hard_mode=True)], lim=16)
ans = min(state.total_mana_spent for state in win_states)
print(ans)
