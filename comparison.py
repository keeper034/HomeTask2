a = input("Введите первое число: ")
if(a.isdigit()):
    a = int(a)
    print("Вы ввели первую цифру " , a)
else:
   print("Вы ввели строку или ничего не ввели ")

b = input("Введите второе число: ")
if(b.isdigit()):
    b = int(b)
    print("Вы ввели вторую цифру " , b)
else:
   print("Вы ввели строку или ничего не ввели")

def compare (a,b):
    x = True
    y = False
    if a > b:
        print(x)
        return x
    else:
        print(y)
        return x

compare(a,b)
