import itertools 

letters = ['a', 'b', 'c', 'd, k']
perms = itertools.permutations(letters)

for perm in perms:
    print(perm)