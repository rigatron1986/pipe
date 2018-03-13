dict1 = {'a': [1], 'b': [2]}
dict2 = {'b': [3], 'c': [4]}
import copy
import itertools


def merge(a, b, conflict):
    new = copy.deepcopy(a)
    if conflict:
        for key, value in b.items():
            if key in new:
                counter = itertools.count(1)
                # Rename 1st key.
                while True:
                    name = '{}_{}'.format(key, next(counter))
                    if name not in new:
                        new[name] = new[key]
                        del new[key]
                        break
                # Create 2nd key.
                while True:
                    name = '{}_{}'.format(key, next(counter))
                    if name not in new:
                        new[name] = value
                        break
            else:
                new[key] = value
    else:
        for key, value in b.items():
            new.setdefault(key, []).extend(value)
    return new
print merge(dict1, dict2, True)
print merge(dict1, dict2, False)
