# There is a difference between Class and Instance Variables
# Class Variables are shared across all class instances
# Instance Variables are NOT shared across all classes

# Class Variables
# So if we just have a variable defined at the classes
# base level indentation and outside of any __init__()
# method definition then we will be able to access that
# same variable across ALL (EVERY) class created.

# Instance Variables
# While the instance variables is created INSIDE of an
# __init__() method definition will only be able to be
# affected on a PER Class Instance basis. Meaning, if
# we have a health INSTANCE VARIABLE for a Class and
# we have a class Human and andrew = Human() and we
# update the Health for andrew, then ONLY andrew has
# an updated health, otherwise it would be Class scoped
# variable and every Human's health would be updated.

# Generally speaking, unless the property has something
# to do with every single class member then we do not
# want to use Class Variables, if you need to use one
# you will know, think of Class Variables them like
# GLOBAL VARIABLES!

# Example(s):

class Human:
    species = "Human"

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        if self.health <= 0:
            raise Exception("Player has no health, cannot take damage.")
        else:
            self.health -= damage

    def __str__(self):
        return f"{self.name} is a {self.species} with {self.health}."

andrew = Human("Andrew", 100)
julia = Human("Julia", 100)

andrew.take_damage(20)
print(f"{andrew.name} damage taken was 20, new health is {andrew.health}.")

julia.take_damage(30)
print(f"{julia.name} damage taken was 30, new health is {julia.health}.")

print(f"Andrew is of the species: {andrew.species}")
print(f"Julia is of the species: {julia.species}")

Human.species = "Alien"

print(f"Now Andrew is a {andrew.species}")
print(f"Now Julia is a {julia.species}")

print("Now our Humans are actually Aliens")
