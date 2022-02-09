from random import randint
from datetime import datetime

secret = randint(1, 100)

number = None
c = 0
start = datetime.now()
while True:
    c += 1
    try:
        number = int(input("Я выбрал рандомное число от 1 до 100 угадай какое это число:"))
        if number > 100:
            print("Вводите число меньше 100")
        elif secret < number:
            print("<")
        elif number < 0:
            print("Введите число больше 0")
        elif secret > number:
            print(">")
        else:
            print(f"Вы угадали поздровляю - {secret}")
            break
        if secret + 5 >= number >= -5:
            if number < secret:
                print("Очень Близко")
            else:
                print("Очень Близко")
        elif secret + 10 >= number >= secret - 10:
            if number < secret:
                print("Близко")
            else:
                print("Близко")
    except ValueError:
        print("Ошибка введите число так как у вас просит игра")
end = datetime.now()

print(f"Время проведенное в игре составило: {end - start}")
print(f"Вы использовали попыток: {c}")
