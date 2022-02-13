import random as r

hp = 0
coins = 0
damage = 0

def printParameters():
    print("У тебя осталось {0} жизней, {1} монет и {2} уроан.". format(hp, coins, damage))

def printHp():
    print("У тебя", hp, "жизней.")

def printCoins():
    print("У тебя", coins, "монет.")

def printDamage():
    print("У тебя", damage, "урона.")

def meetShop():
    global hp
    global coins
    global damage

    def buy(cost):
        global  coins
        if coins >= cost:
            coins -= cost
            printCoins()
            return True
        print("У тебя маловато монет!")
        return False

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5)
    weapons = ["AK-47", "Железный меч", "Лопата", "Лук", "Палка-копалка"]
    weaponRarities = ["Стандарт", "Редкий", "Легендарный"]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    print("На пути тебе встретился торговец!")
    printParameters()

    while input("Что ты будешь делать (зайти/выйти): ").lower() == "зайти":
        print("1) Одна единица здоровья -", oneHpCost, "монет;")
        print("2) Три единицы здоровья -", threeHpCost, "монет;")
        print("3) {0} {1} - {2} монет.".format(weaponRarities, weapon, weaponCost))

        choice = input("Что хочешь приобрести: ")
        if choice == "1":
            if buy(oneHpCost):
                hp += 1
                printHp()
        elif choice == "2":
            if buy(threeHpCost):
                hp += 3
                printHp()
        elif choice == "3":
            if buy(weaponCost):
                damage = weaponDmg
                printDamage()
        else:
            print("Я такое не продаю.")

def meetMonster():
    global hp
    global coins

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Little boy", "Clown", "Creper", "Frank", "Bob"]
    monster = r.choice(monsters)

    print("Ты набрел на монстра - {0}, у него {1} уровень, {2} жизней и {3} урона.".format(monster, monsterLvl, monsterHp, monsterDmg))
    printParameters()

    while monsterHp > 0:
        choice = input("Что будешь делать (удар/убежать): ").lower()

        if choice == "удар":
            monsterHp -= damage
            print("Ты атаковал монстра и у него осталось", monsterHp, "жизней.")
        elif choice == "убежать":
            chance = r.randint(0, monsterLvl)
            if chance == 0:
                print("Тебе удалось сбежать с поля боя!")
                break
            else:
                print("Монстр оказался быстрым и догнал тебя.")
        else:
            continue

        if monsterHp > 0:
            hp -= monsterDmg
            print("Монстр атаковал и у тебя осталось", hp, "жизней.")

        if hp <= 0:
            break
    else:
        loot = r.randint(0, 2) + monsterLvl
        coins += loot
        print("Тебе удалось одолеть монстра, за что ты получил", loot, "монет.")
        printCoins()


def initGame(initHp, initCoins, initDmg):
    global hp
    global coins
    global damage

    hp = initHp
    coins = initCoins
    damage = initDmg

    print("Ты отправился в странствие навстречу приключения и опасностям. Удачного путешествия!")
    printParameters()

def gameLoop():
    situation = r.randint(0, 10)
    if situation == 0:
        meetShop()
    elif situation == 1:
        meetMonster()
    else:
        input("Блуждаю...")

initGame(3, 5, 1)

while True:
    gameLoop()

    if hp <= 0:
        if input("Хочешь начать сначала (да/нет):").lower() == "да":
            initGame(3, 5, 1)
        else:
            break


