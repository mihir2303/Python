class animal():
    def sound(self):
        print("Animal Sound")
        
class Dog(animal):
    def bark(self):
        print("Dog is Barking")
        
class Dogbaby(Dog):
    def eat(self):
        print("Dog baby is writing")
        
d=Dogbaby()
d.sound()
d.bark()
d.eat()