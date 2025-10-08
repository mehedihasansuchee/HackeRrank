#Detect Floating Point Number


import re

responses = []

t = int(input())

for _ in range(t):
    s = input().strip()
    pattern = r"^[+-]?[0-9]*\.[0-9]+$"
    responses.append(bool(re.match(pattern, s)))

for _ in range(t):
    print(responses[_])