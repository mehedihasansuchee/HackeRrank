#Set Mutations


len_a = int(input())
a = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    operation = input().split()[0]
    other_set = set(map(int, input().split()))

    if operation == "update":
        a.update(other_set)
    elif operation == "intersection_update":
        a.intersection_update(other_set)
    elif operation == "difference_update":
        a.difference_update(other_set)
    elif operation == "symmetric_difference_update":
        a.symmetric_difference_update(other_set)

print(sum(a))



'''def updateit(setA,s,command):
    if command == "update":
        setA.update(s)
    elif command == "difference_update":
        setA.difference_update(s)
    elif command == "intersection_update":
        setA.intersection_update(s)
    else :
        setA.symmetric_difference_update(s)
    return setA

a = int(input())
setA = set(map(int,input().split()))

for i in range(int(input())):
    command,len_of_set = input().split()
    s = set(map(int, input().split()))
    setA = updateit(setA,s,command)
print(sum(setA))'''