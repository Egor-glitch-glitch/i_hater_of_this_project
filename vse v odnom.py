import math
z = input("Выберите Задание")
if z == "1":
    n = int(input())
    if 2 <= n <= 100:
        prices = list(map(int, input().split()))
        
        if len(prices) == n:
            valid_prices = True
            for price in prices:
                if not (0 <= price <= 10**9):
                    valid_prices = False
                    break
            
            if valid_prices:
                result = [-1] * n
                for i in range(n):
                    for j in range(i + 1, n):
                        if prices[j] < prices[i]:
                            result[i] = j
                            break  
                print(' '.join(map(str, result)))
            else:
                print("Ошибка в ценах")
        else:
            print("Ошибка в количестве городов")
elif z == "2":
    a = list()
    c = list()
    while True:
        n = str(input())
        c.append(n)
        for i in n:
            if i ==" ":
                d = n[len(i)+3::]
                d = int(d)
                a.append(d)
                print("ok")
            else:
                pass
        if n =="pop":
            if len(a) != 0:
                a.pop(0)
            else:
                print("У тебя в галаве пуста error")
        if n == "front":
            if len(a) != 0:
                print(a[0])
            else:
                print("У тебя в галаве пуста error")
        if n == "size":
            print(len(a))
        if n == "clear":
            print("Вы уверены?")
            s = str(input("Да или Нет"))
            if s == "Да":
                a.clear()
            else:
                continue
        if n == "exit":
            print("Пака")
            break
        else:
            continue
    print(f"Список символов:{a}")
    print("Список команд:")
    for i in c:
        print(i)
elif z == "3":
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
elif z == "4":
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
else:
    print("Нет ничего")