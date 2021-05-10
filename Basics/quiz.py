'''
Created on Aug 7, 2017

@author: summertech
'''
num=0
num2=0
def printquestion(question,x1,x2,x3,x4,ans):
    global num
    num=0
    global num2
    num2=0
    print("--------------------------------")
    print("***********************")
    print (question)
    print ("---------------------")
    print ("a: "+x1+"  |  b: "+x2+"  |  c: "+x3+"  |  d: "+x4)
    print("***********************")
    quest=input("Answer Goes Here: ")
    if ans==quest:
        print("Correct!")
        num+=1
    elif ans!=quest:
        print("Incorrect! The Answer Was {}".format(ans))
        num2+=1
question1="What color is the sky??"
a1="Blue"
a2="Red"
a3="Pinkalicious"
a4="The Sky Doesn't Exist"
printquestion(question1,a1,a2,a3,a4,"d")
question2="What color is the moon??"
b1="Purple"
b2="Red"
b3="Pinkalicious"
b4="What is a moon?"
printquestion(question2,b1,b2,b3,b4,"a")
question2="Why?"
b1="Idunno"
b2="BECAUSE"
b3="DONT ASK"
b4="I'm Still Confused, What is a moon?"
printquestion(question2,b1,b2,b3,b4,"c")
que=num+num2


