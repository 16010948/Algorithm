import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

MAX = int(10 ** 9)

def gcd(a, b):
    if b == 0:
        return str(a)
    return gcd(b, a % b)

n = int(input())
a = 1
for num in list(map(int, input().split())):
    a *= num

m = int(input())
b = 1
for num in list(map(int, input().split())):
    b *= num

print(gcd(a, b)[-9:])