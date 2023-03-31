print('Введите что интересует:\n1)login.\n2)parol.\n3)code.\n4)Exit.')
vk={1:'login: sasha123',2:'parol: 2043212',3:'code: 3213'}
vvod=float(input('Цифра: '))
try:
    while vvod<4:
        print(vk[vvod])
        vvod = float(input('Что-то еще? Цифра: '))
        if vvod>4 or vvod<0:
            print('Ошибка')
            break
except ValueError:
    print('Долбаеб? тут цифры..перезапусти')
