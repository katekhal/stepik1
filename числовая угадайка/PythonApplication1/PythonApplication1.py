import random
newgame = "+"

def is_valid(n):
    return n.isdigit() and 1<=int(n)<=border


flag = True
counter = 0
while newgame == "+":
    print('Добро пожаловать в числовую угадайку')
    border = int(input("Введите границу диапазона: "))
    print('Угадайте число от 1 до', border)
    num = random.randrange(1, border+1)
    while flag:
        counter +=1
        print('Введите число')
        chislo = input()
        if is_valid(chislo):
            chislo = float(chislo)
            if chislo < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            if chislo > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            if chislo == num:
                print('Вы угадали, поздравляем!')
                flag = False
                print('Число попыток = ', counter)
                
        else:
            print('А может быть все-таки введем целое число от 1 до', border)
    print('Если хотите сыграть еще раз напишите "+"')
    newgame = input()
print('Спасибо, что играли в числовую угадайку')

        


