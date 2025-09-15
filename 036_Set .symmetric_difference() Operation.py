#Set .symmetric_difference() Operation


n_english = int(input())
sub_english = set(map(int, input().split()))

n_french = int(input())
sub_french = set(map(int, input().split()))

result = sub_english.symmetric_difference(sub_french)

print(len(result))