# Any variable can be unpacked
p = (4, 5)
x, y = p
data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
name, shares, price, (year, mon, day) = data
# An error is thrown if there is a mismatch
# works with any iterable object
