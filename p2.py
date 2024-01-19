class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name}")
        print(f"{self.age}")
person1 = Person("You",1)
person1.info()
