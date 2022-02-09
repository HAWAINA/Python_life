def user(day,month,name=None):
    if day >= 21 and month == 3 or day <= 20 and month == 4:
        print("овен")
    if day >= 21 and month == 4 or day <= 21 and month == 5:
        print("телец")
    if day >= 22 and month == 5 or day <= 21 and month == 6:
        print("близнецы")
    if day >= 22 and month == 6 or day <= 22 and month == 7:
        print("рак")
    if day >= 23 and month == 7 or day <= 21 and month == 8:
        print("лев")
    if day >= 22 and month == 8 or day <= 23 and month == 9:
        print("дева")
    if day >= 24 and month == 9 or day <= 23 and month == 10:
        print("весы")
    if day >= 24 and month == 10 or day <= 23 and month == 11:
        print("скорпион")
    if day >= 24 and month == 11 or day <= 22 and month == 12:
        print("стрелец")
    if day >= 23 and month == 12 or day <= 20 and month == 1:
        print("козерог")
    if day >= 21 and month == 1 or day <= 19 and month == 2:
        print("водолей")
    if day >= 20 and month == 2 or day <= 20 and month == 3:
        print("рыбы")

userDay = int(input("введите день рождение(в цифрах): "))
userMonth = int(input("введите месяц рождение (в цифрах): "))

user(userDay,userMonth)
print(user)