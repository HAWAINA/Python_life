import random


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'{self.__name} health: {self.health} [{self.damage}]'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, boss, heroes):
        for hero in heroes:
            if boss.health > 0 and hero.health > 0:
                hero.health = hero.health - boss.damage


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_ability(self, boss, heroes):
        pass


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health = hero.health + self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 5


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REPULSE")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                self.damage = self.damage + boss.damage
                pass

class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "STUN")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage
        if Thor in heroes:
            hero.__super_ability = boss.damage(0)


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "GENERAL PROTECTION")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage
        if Golem in heroes:
            hero.__super_ability = hero.health / 5

class Witcher(Hero):
    def __init__(self, name, health):
        super().__init__(name, health, None, "DIVINE POWER")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass

class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "INVISIBILITY")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass

class Druid(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "ANGEL")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "TAKE HEALTH")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "FAKE DEAD")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass


class AntMan(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REINCARNATION")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                pass



round_number = 0


def print_statistics(boss, heroes):
    print(f'{round_number} ROUND -----------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print("Heroes won!!!")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(boss, heroes)
    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("OverLord", random.randint(700, 1000), 50)
    warrior = Warrior("Soup", random.randint(250, 300), 10)
    medic_1 = Medic("Doc", random.randint(220, 240), 5, 15)
    medic_2 = Medic("Pavel", random.randint(270, 300), 10, 5)
    magic = Magic("Samuel", random.randint(250, 300), 20)
    berserk = Berserk("Homer", random.randint(170, 250), 8)
    thor = Thor("Odin", random.randint(230, 300), 13)
    golem = Golem("Amogus", random.randint(400, 700), 5)
    witcher = Witcher("Lola", random.randint(250, 320))
    avrora = Avrora("Piper", random.randint(150,220), 14)
    druid = Druid("Leon", random.randint(200, 280), 10)
    hacker = Hacker("Pops", random.randint(150, 220), 15)
    trickybastard = TrickyBastard("Sanny", random.randint(220, 280), 16)
    antman = AntMan("Pickl", random.randint(250, 320), random.randint(15, 20))
    heroes = [warrior, medic_1, medic_2, magic, berserk, thor, golem, witcher, avrora, druid, hacker, trickybastard, antman]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()

