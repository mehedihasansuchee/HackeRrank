#itertools.permutations()


from itertools import permutations

string, k = input().split()

for item in sorted(list(permutations(string, int(k)))):
    print(''.join(item))