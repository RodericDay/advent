'''

"" is 2 characters of code (the two double quotes), but the string contains zero characters.
"abc" is 5 characters of code, but 3 characters in the string data.
"aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
"\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.

Disregarding the whitespace in the file, what is the number of characters of
code for string literals minus the number of characters in memory for the values
of the strings in total for the entire file?
'''

text = open('challenge_08.txt', 'rb').read().strip().split(b'\n')
a, b = 0, 0
for line in text:
    a += len(line)
    b += len(eval(line))
print(a-b)

import re

a, b = 0, 0
for line in text:
    a += len(line)
    b += len(re.escape(line.decode()))+2
print(b - a)
