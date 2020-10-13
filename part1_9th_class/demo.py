#import all classes
import practice9_7
#import classes
from practice9_7 import User
# import system models
from collections import OrderedDict


class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll_over(self):
        print(self.name.title()+" rolled over!")

my_dog= Dog('willie',6)
print("My dog's name is "+my_dog.name.title())
print("My dog is "+str(my_dog.age)+" years old")
my_dog.sit()
my_dog.roll_over()

your_dog=Dog("lucy",3)
your_dog.sit()
your_dog.roll_over()

class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+ self.make+" "+ self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+ str(self.odometer_reading)+ " miles on it")
    def update_odometer(self,mileage):
        if mileage>self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer")
        self.odometer_reading=mileage
    def increment_odometer(self,miles):
        self.odometer_reading+=miles



my_new_car= Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

#change mod
#first
my_new_car.odometer_reading=23
my_new_car.read_odometer()

#second
my_new_car.update_odometer(45)
my_new_car.read_odometer()

#third
my_new_car.increment_odometer(10)
my_new_car.read_odometer()

#继承
class ElectriceCar(Car):
    def __init__(self,make,model,year):
        '''use super to get all mod and method from father class
            add new mod
        '''
        super().__init__(make,model,year)
        self.battery_size=70

    def describe_battery(self):
        '''new mod'''
        print("This car has a "+str(self.battery_size)+"-kWh battery")

    def fill_gas_thank(self):
        '''overwrite method from father class'''
        print("This cat doesn't need a gas tank!")



my_tesla=ElectriceCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_thank()

#拆分类
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message= "This car can go approximately "+str(range)
        message+=" miles on a full charge."
        print(message)

class newElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()

new_tesla=newElectricCar('tesla','Model s',2016)
new_tesla.battery.describe_battery()
new_tesla.battery.get_range()

# use system function
favorite_languages=OrderedDict()
favorite_languages['jen']='python'
favorite_languages['sarah']='c'
favorite_languages['edward']='ruby'
favorite_languages['phil']='python'
for name,language in favorite_languages.items():
    print(name.title()+"'s favorite language is "+language.title())

