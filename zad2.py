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
        a.pop(0)
    if n == "front":
        print(a[0])
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
    
print(a,c)