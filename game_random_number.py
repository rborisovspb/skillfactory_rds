import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,100)    # загадали число
print ("Загадано число от 1 до 99")

a = 50
b=1
c=100
while a != number:
    if number>=a:
        print ('Загаданное число больше', a)
        b = a
        a = (c + a)//2
    else:
        print ('Загаданное число меньше', a)
        c = a
        a = (a+b)//2
print ('Загаданное число', a)