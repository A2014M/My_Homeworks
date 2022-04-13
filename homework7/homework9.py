"""создание класса данных"""

from dataclasses import dataclass
from unicodedata import name

@dataclass
class Children:
    name: str
    surname: str
    age: str
    gender: str

child1 = Children("Lisa", "Edelshtein", "12", "female")
child2 = Children("Marat", "Baransky", "11", "male")
child3 = Children("Olga", "Ivanova", "15", "female")
child4 = Children("Maksim", "Petrov", "9", "male")
child5 = Children("Arseniy", "Kutuzov", "7", "male")

print(child1)
print(type(child1))
print(child2)
print(child3)
print(child4)
print(child5)

"""использование классметода"""

class Players():
    total_objects=0

    def __init__(self):
        Players.total_objects = Players.total_objects+1

    @classmethod
    def TOTAL_OBJECTS(cls):
        print('Total objects:' , cls.total_objects)

object1 = Players()
object2 = Players()
object3 = Players()
object4 = Players()
object5 = Players()

Players.TOTAL_OBJECTS()

"""использование статик метода"""

from datetime import datetime
import time

class Players():

    def __init__(self, name, age, born):
        self.name = name
        self.age = age
        self.born = datetime.now()

    def say_hello(self):
        return f'Hello. My name is {self.name}. I am {self.age} years old. I was borneded {self.born}'

    @staticmethod
    def greeting():
        print('You are welcome!')

player1 = Players('Arnold', 23, datetime.now)
print(player1.say_hello())
Players.greeting()
time.sleep(1)

player2 = Players('Alla', 43, datetime.now)
print(player2.say_hello())
Players.greeting()
time.sleep(1)

player3 = Players('Marusya', 29, datetime.now)
print(player3.say_hello())
Players.greeting()
