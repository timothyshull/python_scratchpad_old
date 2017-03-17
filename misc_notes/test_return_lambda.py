import operator


# def gen_min_max_validator(local_min=None, local_max=None, include=False):
#     if local_min and local_max:
#         if include:
#             def min_max_validator(val):
#                 return local_min <= val <= local_max
#         else:
#             def min_max_validator(val):
#                 return local_min < val < local_max
#     elif local_max:
#         if include:
#             def min_max_validator(val):
#                 return val <= local_max
#         else:
#             def min_max_validator(val):
#                 return val < local_max
#     elif local_min:
#         if include:
#             def min_max_validator(val):
#                 return local_min <= val
#         else:
#             def min_max_validator(val):
#                 return local_min < val
#     else:
#         # noop if no args given
#         def min_max_validator(*args):
#             return True
#     return min_max_validator

def gen_min_max_validator(local_min=None, local_max=None, include=False):
    comparator = operator.ge if include else operator.gt

    return lambda x: (comparator(x, local_min) if local_min else True) and \
                     (comparator(local_max, x) if local_max else True)


validator = gen_min_max_validator(local_min=1, local_max=10, include=True)

print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))

print("Without include")
validator = gen_min_max_validator(local_min=1, local_max=10, include=False)

print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))

print("Just max")
validator = gen_min_max_validator(local_max=10, include=True)
print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))

print("Just min")
validator = gen_min_max_validator(local_min=1, include=True)
print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))

print("Just max without include")
validator = gen_min_max_validator(local_max=10, include=False)
print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))

print("Just min without include")
validator = gen_min_max_validator(local_min=1, include=False)
print(validator(11))
print(validator(10))
print(validator(9))
print(validator(2))
print(validator(1))
print(validator(0))
