import sys
import math


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
    return d


d = {}
print(update_dictionary(d, 1, -1))  # None
print(d)                            # {2: [-2]}
update_dictionary(d, 2, -2)
print(d)                            # {2: [-2, -2]}
update_dictionary(d, 1, -3)
print(d)                            # {2: [-2, -2, -3]}