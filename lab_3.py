def z1():
    word = ""
    k = 0
    while k == 0:
        slovo = input("Введите слово: ")
        if slovo == 'stop':
            k = 1
        else:
            k = 0
            word += slovo + " "
    print(word)

def z2():
    word = str(input("Введите слово: "))
    if 'Ф' in word or 'ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово...')

def z3():
    import random
    e = 0
    k = 0
    while e != 3:
        a = random.randint(0,100)
        b = random.randint(0,100)
        print(f'{a}+{b}=', end='')
        c = input()
        while not (c.isdigit() and c != 'stop'):
            print('Введите численное значение: ', end='')
            c = input()
        if c == 'stop':
            break
        if a+b == int(c):
            print('Правильно!')
            k += 1
        else:
            print('Ответ неверный')
            e += 1
    print('Игра окончена. Правильных ответов: ', k)

z3()