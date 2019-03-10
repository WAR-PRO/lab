import random

number = random.randint(0, 100)
question = False
while question == False:
    kavo = int(input('Введите ваше число:'))
    if kavo == number:
        print('Число отгадано')
        question = True
    else:
        if kavo > number:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')

