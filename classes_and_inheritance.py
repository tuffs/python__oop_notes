# Classes and Inheritance in the Python Language
#---

# When a class is defined in Python, we do
# the following for a class with the name Plant.

class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # Our methods (functions inside classes),
    #must include self before other parameters

    def grow(self, amount):
        self.height += amount

    # The __str__ method on a class gives a string
    # response to identify a class in itself
    def __str__(self):
        return f"{self.name} is {self.height} meters tall."

# Let's call our new class a 'Tree' with
# the height of 20 meters

p = Plant("Tree", 20)

# Now, we are going to call the Plant classes grow()
# method which takes an integer for the amount of
# meters to grow

p.grow(120) # grows 120m, so 20m + 120m = 140m

# Finally, to finish the use of the Plant class
# let's call the __str__ class method by simply
# calling for the instance of the class itself
# to be printed like so.

print(f"{p}")

# * * * * * * * * * * * * * * * * * * * * * >

# ANY METHOD ON A CLASS WILL ALWAYS TAKE SELF
# AS A PARAMETER!!

# * * * * * * * * * * * * * * * * * * * * * >

# Subclasses are defined with syntax:
# `class Subclass(Parentclass):`


# When we have a subclass of a parent class
# such as Tree from Plant. We will always have
# a constructor class (`__init__`) which will take
# the original parameters from the parent class
# in order to properly initialize that subclass
# as a child of the parent class.

# This will happen with the following psuedo-code:
# `super().__init__(parent,arguments,here)`

# Let's build a subclass of Plant called Tree

class Tree(Plant):
    def __init__(self, name, height): # note that we are taking self, name, height -- always take self, name and height are
        super().__init__(name, height) # brought in from the parent class args here
        self.branches = 0 # then we can add our own properties to the subclass like branches

    def grow_branches(self, new_branches): # then we can define a way to add branches to Tree
        self.branches += new_branches # these are incremented by calling the tree.grow_branches(int) method

    def __str__(self):
        return f"The {self.name} Tree has {self.branches} branches and is {self.height}m tall"

# So, we have initialized the Tree class with
# the properties that are given to the parent
# class on construction. These are then
# properly passed down to the subclass through
# the constructor/initializer method which also
# will always take self.

# We also have a branches property for Trees,
# this is specific to trees as not all Plants
# have branches but all Trees have branches.

# This calls for the creation of the subclass
# specific method on Trees,
# `grow_branches(self, new_branches)`

# Create a subclass, grow the height, and grow branches...
tree = Tree("Pine", 20)
tree.grow(100)
tree.grow_branches(20)

print(f"The {tree.name} has {tree.branches} branches.")
print("")
print(f"Our subclass is: {tree}")

# Also, if we initialize a subclass and it has a new parameter
# the new parameter is provided to the __init__(self,y,z) call
# but not the following super().__init__(y) call where the z is
# new to the subclass and NOT a part of the parent class
# just as in the following example:

class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.name = name
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows

# There are also rules to this thing!
# Be careful of not always inheriting,

# As a rule of thumb:
# "A" should only inherit from "B" if "A" is *always* a "B"!

# For Example:
# - "Cat" should inherit from "Animal" b/c "Cat" is always an "Animal"
# - "Truck" should inherit from "Vehicle" b/c "Truck" is always an "Vehicle"
# - "Lane" should inherit from "BadDotaPlayers" b/c "Lane" is always a "BadDotaPlayer"

# But the following are not true, and you will end up with a mess if you try to *FORCE* them
# - "Cat" should not inherit from "Dog" b/c a "Cat" is not always a "Dog"
# - "Animal" should not inherit from "Cat" b/c an "Animal" is not always a "Cat"
# - "Allan" should not inherit from "Employed" b/c "Allan" is not always "Employed"

# I want to be clear with my motives for learning.

# Classes in Python are defined as:

class Vehicle:
    def __init__(self, manufacturer, model, cost):
        self._manufacturer = manufacturer
        self._model = model
        self._cost = cost

    def set_manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

    def get_manufacturer(self):
        return f"{self._manufacturer}"

    def set_model(self, model):
        self._model = model

    def get_model(self):
        return f"{self._model}"

    def set_cost(self, new_cost):
        self._cost = new_cost

    def get_cost(self):
        return f"${self._cost:,}.00"

    def __str__(self):
        manufacturer = f"{self._manufacturer}"
        model = f"{self._model}"
        cost = f"${self._cost}.00"
        return f"{manufacturer} {model} is {cost}"


# So, let's make a vehicle from the class!
porsche = Vehicle("Porsche", "996", 256_000)
print(f"{porsche}")

# An invitation to read the printed statement
print("So we are speaking of cars, let's go!")

# some breathing room...
print("")
print("---")
print("")
# trying to print manufacturer from the class method
print(f"The {porsche.get_manufacturer()} {porsche.get_model()} is about {porsche.get_cost()} to purchase!")
