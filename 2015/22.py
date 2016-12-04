import re, collections, types

GameState = collections.namedtuple("GameState", "player_hp player_mp enemy_hp enemy_atk ongoing")
Spell = collections.namedtuple("Spell", "cost duration")
spell_book = {
    "Magic Missile": Spell(53, 0),
    "Drain": Spell(73, 0),
    "Shield": Spell(113, 6),
    "Poison": Spell(173, 6),
    "Recharge": Spell(229, 5),
}

def resolve(spell_cast, state, hard=False):
    player_hp, player_mp, enemy_hp, enemy_atk, ongoing = state
    player_turn = spell_cast is not None

    if hard and player_turn:
        player_hp -= 1
        if player_hp < 1: return "loss", None

    # resolve ongoing effects
    ongoing_spells = collections.Counter(ongoing)
    active = set(ongoing_spells.elements())
    ongoing_spells -= {k:1 for k in active}  # decrease cooldown
    player_def = 7 if 'Shield' in active else 0
    player_mp += 101 if 'Recharge' in active else 0
    enemy_hp -= 3 if 'Poison' in active else 0
    if enemy_hp < 1: return "win", None

    if player_turn:
        # casting an active spell is invalid
        if spell_cast in ongoing_spells.elements(): return "invalid", None
        # casting a spell without required mp is invalid
        player_mp -= spell_book[spell_cast].cost
        if player_mp < 0: return "invalid", None
        # assign cooldown
        ongoing_spells[spell_cast] = spell_book[spell_cast].duration
        # handle instantaneous spells
        if spell_cast == 'Magic Missile': enemy_hp -= 4
        if spell_cast == 'Drain': enemy_hp -= 2; player_hp += 2
        # win condition
        if enemy_hp < 1: return "win", None

    else:
        player_hp -= max(1, enemy_atk-player_def)
        if player_hp < 1: return "loss", None

    # state transfer
    ongoing = tuple(ongoing_spells.elements())
    return "ongoing", GameState(player_hp, player_mp, enemy_hp, enemy_atk, ongoing)

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
