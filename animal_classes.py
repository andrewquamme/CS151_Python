class Animal:
    def __init__(self, name):
        self.name = name
        self.type = "animal."
    def sound(self):
        print("Noises.")
    def teeth(self):
        print("I has teeth.")
    def tail(self):
        print("I has a tail.")
   

class Cat(Animal):
    def sound(self):
        print("Meow.")

class Dog(Animal):
    def sound(self):
        print("Woof.")

alfred = Cat("Alfred")
ody = Dog("Ody")

print("My name is " + alfred.name)
alfred.teeth()
alfred.tail()
alfred.sound()

print("My name is " + ody.name)
ody.teeth()
ody.tail()
ody.sound()
