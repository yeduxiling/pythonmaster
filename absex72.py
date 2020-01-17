import datetime


class Golem:

    def __init__(self, name=None):
        self.name = name
        self.built_year = datetime.date.today().year

    def say_hi(self):
        print('Hi!')

class Running_Golem(Golem):

    def run(self):
        print("Can't you see? I'm running...")

rg = Running_Golem("Clay")
print(rg.run)
print(rg.run())
print(rg.name)
print(rg.built_year)
print(rg.say_hi())
