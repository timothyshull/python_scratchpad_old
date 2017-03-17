f = open('1.json')

print(f.readline())

x = f.readline()

print(type(x) is str)

print(isinstance(x, str))
