#Check Subset


t = int(input())

for _ in range(t):
    n_a = int(input())
    val_a = set(map(int, input().split()))
    n_b = int(input())
    val_b = set(map(int, input().split()))

    print(val_a.issubset(val_b))