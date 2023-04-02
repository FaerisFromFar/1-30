from time import*
a=0

try:
    number_one=int(input('Введи число 1 - '))
    if number_one == int:
        a==1
except(ValueError):
    print('Это не число и (функция 1)')
try:
    number_two = int(input('Введи число 2 - '))
    if number_two == int:
        a==1
except(ValueError):
    print('Это не число и (функция 1)')

if a==1:
    sleep(1)

    slojenie=(print('сложение',number_one+number_two))
    sleep(1)
    vichitanie=(print('вычитание',number_one-number_two))
    sleep(1)
    umnojenie=(print('умножение',number_one*number_two))
    sleep(1)
    delenie=(print('деление',number_one/number_two))
    sleep(1)


    if number_one ==0:
        print('Число один 0')
    elif number_one >0:
        print('Число один больше нуля')
    elif number_one <0:
        print('Число один меньше нуля')

    sleep(1)
    if number_two ==0:
        print('Число два 0')
    elif number_two >0:
        print('Число два больше нуля')
    elif number_two <0:
        print('Число два меньше нуля')
        sleep(1)
        print('среднее арифмитическое - ',(number_one+number_two)/2)

