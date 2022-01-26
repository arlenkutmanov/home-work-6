
while 1:
    value = int(input('Напишите число: '))
    if value < 0 or str(value)!=str(value)[::-1]:
         print(f'не палиндром  {False}\n')
         print(f'Это не универсальное число {value}')
    else:
        print(f'Это универсальное число {value}')
        print(f'палиндром {True}\n')
