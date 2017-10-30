import re

description = '''
The first floor contains a thulium generator, a thulium-compatible microchip, a plutonium generator, and a strontium generator.
The second floor contains a plutonium-compatible microchip and a strontium-compatible microchip.
The third floor contains a promethium generator, a promethium-compatible microchip, a ruthenium generator, and a ruthenium-compatible microchip.
The fourth floor contains nothing relevant.
''' # 31 55
print( sum(2 * sum([4,2,4,0][:x]) - 3 for x in range(1,4)) )
print( sum(2 * sum([8,2,4,0][:x]) - 3 for x in range(1,4)) )
print()

description = '''
The first floor contains a promethium generator and a promethium-compatible microchip.
The second floor contains a cobalt generator, a curium generator, a ruthenium generator, and a plutonium generator.
The third floor contains a cobalt-compatible microchip, a curium-compatible microchip, a ruthenium-compatible microchip, and a plutonium-compatible microchip.
The fourth floor contains nothing relevant.
''' # 33 75
print( sum(2 * sum([2,4,4,0][:x]) - 3 for x in range(1,4)) )
print( sum(2 * sum([6,4,4,0][:x]) - 3 for x in range(1,4)) )
print()

description = '''
The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
The third floor contains nothing relevant.
The fourth floor contains nothing relevant.
''' # 47 71
print( sum(2 * sum([8,2,0,0][:x]) - 3 for x in range(1,4)) )
print( sum(2 * sum([12,2,0,0][:x]) - 3 for x in range(1,4)) )
print()

