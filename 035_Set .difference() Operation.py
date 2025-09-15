#Set .difference() Operation


n_english = int(input())
sub_english = set(map(int, input().split()))

n_french = int(input())
sub_french = set(map(int, input().split()))

only_english = sub_english.difference(sub_french)

print(len(only_english))