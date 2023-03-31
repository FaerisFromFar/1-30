from random import*
from time import*
from colorama import*
c=0
v=0
z=0
a = randrange(1, 15, 1)  # зашли
b = randrange(1, 3, 1)  # вышли
c = c + a  # в салоне
v += a  # всего
if z==True:
    a = randrange(1, 15, 1)  # зашли
    b = randrange(1, 3, 1)  # вышли
if z==False:
    a = randrange(1, 15, 1)  # зашли
    b = randrange(1, 3, 1)  # вышли
def humans(a,b,c,v):
    a = randrange(1, 15, 1)  # зашли
    b = randrange(1, 3, 1)  # вышли
    return a
    return b
    return c
    return v
sleep(1)
print(Style.BRIGHT + Fore.GREEN + 'Автобус начинает движение.\n',Fore.MAGENTA+'- Пассажиров в салоне', c)
sleep(1)
z=0
print(Style.BRIGHT + Fore.CYAN + '----- Едем -----')
sleep(2)
a = randrange(1, 15, 1)  # зашли
b = randrange(1, 5, 1)  # вышли
c = c + a - b  # в салоне
v += a  # всего
print(Style.BRIGHT + Fore.GREEN + 'Прибываем на остановку Технический Университет Имени Павла.\n',Fore.MAGENTA+'- Пассажиров в салоне', c)
sleep(1)
print(Style.BRIGHT + Fore.CYAN + '----- Едем -----')
sleep(2)
a = randrange(1, 10, 1)  # зашли
b = randrange(1, 5, 1)  # вышли
c = c + a - b  # в салоне
v += a  # всего
print(Style.BRIGHT + Fore.GREEN + 'Прибываем на остановку Технический Университет Имени Павла.\n',Fore.MAGENTA+'- Пассажиров в салоне', c)
sleep(1)
print(Style.BRIGHT + Fore.CYAN + '----- Едем -----')
sleep(2)
print(Style.BRIGHT + Fore.GREEN + 'Прибываем на конечную остановку.\n',Fore.MAGENTA+'- Пассажиров в салоне', c)
sleep(1)
print(Style.BRIGHT + Fore.RED + '----- Конец, Идет подсчет... -----')
sleep(3)
n=v/2
print(Style.BRIGHT + Fore.GREEN +'Заработали -',v*0.8,'рубль!')
print(Style.BRIGHT + Fore.RED + 'Расходы - ',n,'рублей..')