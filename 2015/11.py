import string, itertools

password = list(b'hepxcrrq')

a, z = ord('a'), ord('z')
az = list(range(a, z+1))

def increment(password):
    for i, b in reversed(list(enumerate(password))):
        password[i] += 1
        if password[i] > z:
            password[i] = a
        else:
            break

required = sorted(bytes(combo) for combo in zip(az, az[1:], az[2:]))

def check(password):
    password = bytes(password)
    yield any(r in password for r in required)
    yield not any(c in password for c in b'iol')
    s = set()
    for i,(a,b) in enumerate(zip(password, password[1:])):
        if a==b and i-1 not in s:
            s.add(i)
            if len(s)>1:
                return
    yield False

while not all(check(password)):
    increment(password)
print(bytes(password))

increment(password)
while not all(check(password)):
    increment(password)
print(bytes(password))
