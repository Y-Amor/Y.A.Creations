website = input("What website do you need a password for?")
siblingName = {}
passKey1 = input ("Do you have any siblings? ")
if (passKey1 == "yes"):
    amountOfSiblings = int(input("How many siblings do you have?"))

for i in range(amountOfSiblings):
    sibling = input("What is your sibling(s) name?")
    siblingName.update(sibling)

print (siblingName)

