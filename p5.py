class Bird:
    def Die(self):
        return "Can die"

class Mammal:
    def Eat(self):
        return "can eat"

class Bat(Bird, Mammal):
    def Can_sleep(self):
        return "Sleep"

bat12 = Bat()
print(bat12.Die())
print(bat12.Eat())
print(bat12.Can_sleep())
