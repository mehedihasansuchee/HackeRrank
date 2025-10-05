#Any or All


n = int(input())

numbers = list(map(int, input().split()))

print(all(x > 0 for x in numbers) & any(str(x) == str(x)[::-1] for x in numbers))