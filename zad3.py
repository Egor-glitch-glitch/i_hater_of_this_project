import math

s = input().strip()
a = list(map(float, s.split()))

if len(a) == 1:
    r = [] if a[0] != 0 else [0]
elif len(a) == 2:
    b, c = a
    r = [] if b == 0 and c != 0 else [-c/b] if b != 0 else [0]
else:
    p, q, w = a
    d = q*q - 4*p*w
    if d > 0:
        x1 = (-q + math.sqrt(d))/(2*p)
        x2 = (-q - math.sqrt(d))/(2*p)
        r = sorted([x1,x2])
    elif d == 0:
        r = [-q/(2*p)]
    else:
        print("Ни уравнение")
        r = []

print(r)