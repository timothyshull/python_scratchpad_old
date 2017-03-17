def stackoverflow(x_list, target):
    memo = dict()
    result, _ = g(x_list, x_list, target, memo)
    return sum(result), result


def g(v, w, s, memo):
    subset = []
    id_subset = []
    for i, (x, y) in enumerate(zip(v, w)):
        # Check if there is still a solution if we include v[i]
        if f(v, i + 1, s - x, memo) > 0:
            subset.append(x)
            id_subset.append(y)
            s -= x
    return subset, id_subset


def f(v, i, s, memo):
    if i >= len(v):
        return 1 if s == 0 else 0
    if (i, s) not in memo:  # <-- Check if value has not been calculated.
        count = f(v, i + 1, s, memo)
        count += f(v, i + 1, s - v[i], memo)
        memo[(i, s)] = count  # <-- Memoize calculated result.
    return memo[(i, s)]  # <-- Return memoized value.

if __name__ == "__main__":
    stackoverflow([2, 3, 4], 10)
