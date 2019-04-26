
# coding: utf-8

# In[35]:


# Prototype

# Some prerequisites for prototype example

# function accepting arbitrary variables

def f(**attrs):
    print (attrs)
    
f(x = 1, y = 2, z = 3)

# Get the vanilla, reinitialized class back from an instance 

class example:
    def __init__(self):
        self.var = 1
    def set_var(self, n):
        self.var = n

e = example()
print(e.var)
e.set_var(10)
print(e.var)
e_class = e.__class__()
print(e_class.var)

# get the variables of a class as a dictionary

print(e_class.__dict__)


# Prototype

# Reduce the number of different kinds of classes
# Creates objects by cloning a prototype instance at runtime
# Uses a Dispatcher/Registry/Manager - which allow clients to query for instances
# Useful when instantiation is expensive

class Prototype:
    def clone(self, **attrs):
        cloned_class = self.__class__() # Prototype of an inherited class using it's parameters
        cloned_class.__dict__.update(attrs) 
        return cloned_class

class Dispatcher:
    def __init__(self):
        self.objects = {}
    def get_all_objects(self):
        return self.objects
    def add_object(self, name, obj):
        self.objects[name] = obj
    def delete_object(self, name):
        if name in self.objects:
            del self.objects[name]

d = prototype.clone()
class_prototype_1 = prototype.clone(a = 1, b = True) # supposing a and b were had to get
class_prototype_2 = prototype.clone(a = 'text', b = {1:2, 3:4})

dispatcher = Dispatcher()
dispatcher.add_object('class_prototype_1', class_prototype_1)
dispatcher.add_object('class_prototype_2', class_prototype_2)
dispatcher.add_object('d', d)
print(dispatcher.get_all_objects())
dispatcher.delete_object('d')
print(dispatcher.get_all_objects())


# In[25]:


# Factory pattern

# Creates objects without having to specify the class. 
# A function which returns an instance of a class based on the input

class class1:
    
    def __init__(self):
        pass

    def f(self, num1, num2):
        # Sum two numbers
        return num1 + num2

    
class class2:
    
    def __init__(self):
        pass

    def f(self, num1, num2):
        # Multiply two numbers
        return num1 * num2

def factory(condition):
    if condition == 1:
        return class1()
    else:
        return class2()

a = factory(1)
b = factory(2)

print(a.f(4,2))
print(b.f(4,2))


# In[28]:


# Builder

# Separate the creation of an object with it's representation
# The same process can be used to create objects of the same family
# We have a assembler which builds a defined class (car, house, environment). 
# This assembler takes as input different kinds of builders which construct individual components//
# of the above class

class house_assembler():
    def __init__(self, builder):
        self.__builder = builder
    def assemble(self):
        new_house = house()
        new_house.set_floor(self.__builder.build_floor())
        new_house.set_walls(self.__builder.build_walls())
        new_house.set_ceiling(self.__builder.build_ceiling())
        return new_house
  
    
class house:
    def __init__(self):
        # default parameters
        self.floor = 0
        self.walls = 0
        self.ceiling = 0
    
    def set_floor(self, n):
        self.floor = n

    def set_walls(self, n):
        self.walls = n

    def set_ceiling(self, n):
        self.ceiling = n
    
    def describe(self):
        print ('Floor:', self.floor, 'Walls:', self.walls, 'Ceiling:', self.ceiling)
             
class tent_builder:
    def build_floor():
        return 1
    def build_walls():
        return 3
    def build_ceiling():
        return 0
    
class one_bhk_builder:
    def build_floor():
        return 1
    def build_walls():
        return 4
    def build_ceiling():
        return 1
    
new_one_bhk = house_assembler(one_bhk_builder).assemble()
new_one_bhk.describe()

new_tent = house_assembler(tent_builder).assemble()
new_tent.describe()

