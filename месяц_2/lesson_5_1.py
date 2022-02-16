from random import randint
from calculator import addition as add_two_numbers
from person import Person
from termcolor import cprint
import os
from envparse import env

print(randint(1, 5))
print(add_two_numbers(6, 7))
man = Person("John", 23)
cprint(man, "red")

cprint("hello", "green", attrs=["underline"])

user_name = os.environ.get("DB_USER")
user_pass = '31312sdada'
print(user_name)

env.read_envfile('vars.env')
print(os.environ.get('PYTHON'))
print(os.environ.get('MY_AGE'))
