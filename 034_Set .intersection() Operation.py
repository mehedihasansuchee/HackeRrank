#Set .intersection() Operation


n_english = int(input())
sub_eng = set(map(int, input().split()))
n_fr = int(input())
sub_fr = set(map(int, input().split()))

intersection_sub = sub_eng.intersection(sub_fr)

print(len(intersection_sub))