'''
Created on Aug 11, 2017

@author: coditum
'''
class restaurant(object):
    def __init__(self,takingOrder,deliveringOrder,chefstatus,customers,mngr,isOpen):#Is or isnt
        self.takingOrder=takingOrder
        self.deliveringOrder=deliveringOrder
        self.chefstatus=chefstatus
        self.customers=customers
        self.mngr=mngr
        self.isOpen=isOpen
    def printWaiterStatus(self):
        print("The Waiter currently "+self.takingOrder+" taking an order")
        print("The Waiter currently "+self.deliveringOrder+" delivering an order")
    def printChefStatus(self):
        print("The chef is "+self.chefstatus)
    def printCustomers(self):
        print("There are currently {} customers in the restaurant".format(self.customers))
    def printMngr(self):
        print("The Manager is {}".format(self.mngr))
    def checkIsOpen(self):
        if self.isOpen == False:
            print("This restaurant is closed, forever")
        else:
            print("This restaurant is open")
restaurant=restaurant("isn't","isn't","pooping",0.5,"dead on the toilet next to the chef",False)
restaurant.printWaiterStatus()
restaurant.printChefStatus()
restaurant.printCustomers()
restaurant.printMngr()
restaurant.checkIsOpen()