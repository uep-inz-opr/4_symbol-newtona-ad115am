import math

numbers = list(map(int, input().split()))
n = numbers[0]
k = numbers[1]
result= math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
print(result)