import math

a = int(input())
b = int(input())
mode = int(input())

powerResult = int(math.pow(a,b))
modeResult = pow(a,b,mode)
print(powerResult)
print(modeResult)