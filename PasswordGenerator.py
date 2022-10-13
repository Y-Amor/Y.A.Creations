from ast import While
from asyncio.windows_events import NULL
import random

#Asks the user which website they would need the password for
website = input("What website do you need a password for?" + " ")

#Lists to store the user informations
siblingName = []
luckyNumber = []
age = []

#list of possible endings for complexity in the password
passEnd = ["?" , "!" , "#"]

passKey1 = input ("Do you have any siblings? " + " ")
while (passKey1 == "yes"):
    amountOfSiblings = int(input("How many siblings do you have?" + " "))
    for i in range(amountOfSiblings):
                siblingName.append(input("What is the name of one of your siblings?" + " "))
    number = input("Do you have a lucky number? " + " ")
    if (number == "yes"):
        luckyNumber.append(int(input("What is your lucky number?" + " ")))
    askAge = int(input("How old are you?" +  " "))
    age.append(askAge)

    print ("Your random password for " + website + " " + "is" + " " ,end= ' ')
    print (random.choice(luckyNumber), end= '')
    print (random.choice(siblingName), end= '')
    print(random.choice(age), end = '')
    print(random.choice(passEnd))

    newPass = input("Do you need another password? ") 
    if (newPass == "no" or newPass == "No"):
        passKey1 == NULL
        print("Thank you for using our password generator!")
    else:
        sameWebsite = input ("Is it for the same website?" + " ")
        if (sameWebsite == "yes" or sameWebsite == "Yes"):
            print ("Your new random password for " + website + "is" + " " ,end= ' ')
            print (random.choice(luckyNumber), end= '')
            print (random.choice(siblingName), end= '')
            print(random.choice(age), end = '')
            print(random.choice(passEnd))
            print ("Thank you for using our password generator!")
            passKey1 == "no"
        else: 
            passKey1 == "yes"





    
