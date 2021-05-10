'''
Created on Aug 11, 2017

@author: coditum
'''
class car(object):
    def __init__(self, make, totalMileage):
        self.make = make
        self.isOn = False
        self.totalMileage = totalMileage
        
    def printMake(self):
        print("This car is a " + self.make)
    def checkIsOn(self):
        if self.isOn == False:
            print("This car is off")
        else:
            print("This car is on")
    def checkTotalMileage(self):
        print("The total mileage on this car is " + str(self.totalMileage))
    def addTotalMileage(self, n):
        self.totalMileage = self.totalMileage + n
        
toyota = car("Toyota", 1000)
toyota.printMake()
b = car("ford", 0)
b.printMake()