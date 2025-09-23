# MUST RUN FILE AFTER READING CODE FOR EXAMPLE TO BE COMLPETE


# An Object is an Instance of a Class
# ---
# Example One:
# ---
# Our Soldier class when instantiated anew with a new variable creates a class

class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier("Legolas", 5, 1)
print(soldier_one)

# Now, we are going to have the __str__ method return something
# to not just provide the object placeholder for the class when
# printing to "stdout"

print("")
print("")
print("")

class Beer:
    def __init__(self, brand, name, percent_by_volume):
        self.brand = brand
        self.name = name
        self.__alcohol = percent_by_volume

    def get_alcohol_percent(self):
        return self.__alcohol

    def __str__(self):
        return f"{self.brand} is known as {self.name} and has a(n) {self.get_alcohol_percent()} alcohol content"

budweiser = Beer("Budweiser", "Bud Light", "3.9%")

print(budweiser)
print("")
print(f"The Alc. per mL percent is: {budweiser.get_alcohol_percent()}")

