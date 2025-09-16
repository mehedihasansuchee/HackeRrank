#Collections.OrderedDict()


from collections import OrderedDict

n = int(input())
data = OrderedDict()
for i in range(n):
    inp = input().rpartition(" ")
    data[inp[0]] = data.get(inp[0], 0) + int(inp[2])
for key in data.keys():
    print(key, data[key])