#Loops
'''The provided code stub reads an integer,n,
from STDIN. For all non-negative integers i < n, print i^2.'''

def power (num):
    for i in range(num):
        print(i * i)

if __name__ == '__main__':
    n = int(input())
    power(n)