x = open('1.json').readline()

print(x)

y = x.split('{')

print(y)

t = open('2.json').read().strip()

u = t.splitlines()

print(u)


