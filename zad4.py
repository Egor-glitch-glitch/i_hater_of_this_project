n = list(map(int, input().split()))
a = list(map(int, input().split()))
hod = 0
max_hod = 100
while len(n) > 0 and len(a) > 0 and hod < max_hod:
    n = n.pop(0)
    a = a.pop(0)
    if n > a:
        n.extend([n, a])
    else:
        a.extend([a, n])
        
    hod += 1
if len(n) == 0:
    print("second", hod)
elif len(a) == 0:
    print("first", hod)
else:
    print("unknown", hod)