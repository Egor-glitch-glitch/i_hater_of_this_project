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