import math

def newton():
    numbers = list(map(int, input().split()))
    n = numbers[0]
    k = numbers[1]
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(newton())