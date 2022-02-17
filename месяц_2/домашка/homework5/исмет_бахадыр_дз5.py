import os
import random
from envparse import env

class Casino:
    def __init__(self):
        self.__cash = int(os.environ.get('MY_MONEY'))

        while int(self.__cash) > 0:
            print (f"at the moment you have chips on: {self.__cash}")
            self.__win_slot = random.randint(1, 30)
            print(self.__win_slot)
            self.__slot = int(30)
            self.__bet = int(input('make your bet: '))
            if self.__bet > self.__cash:
                print("you don't have enough money")
            else:
                self.__choice = int(input('select the slot: '))
                if self.__choice > self.__slot:
                    print("no such slot")
                    ans = input('do you want to play more?(yes or write any words): ')
                    if ans != 'yes':
                        break

                if self.__win_slot == self.__choice:
                    self.__cash += self.__bet
                    print(f'You win\n money: {self.__cash}')
                    if self.__win_slot == self.__choice:
                        ans = input('do you want to play more?(yes or write any words): ')
                        if ans != 'yes':
                            break

                else:
                    self.__cash -= self.__bet
                    print(f' You lost \n money: {self.__cash}')
                    if self.__win_slot != self.__choice:
                        ans = input('do you want to play again?(yes or write any words): ')
                        if ans != 'yes':
                            break

    @property
    def win(self):
        return self.__win_slot

    @win.setter
    def win(self, value):
        self.__win_slot = value

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        self.__slot = value


env.read_envfile('settings.env')