questionsTotal=int(input("How many questions do you need to study "))

questionBank = {}

#Gets the users Questions and Answers 
for i in range(questionsTotal):
    question = input("Add your question ")
    answer = input ("What is the answer to that question? ")
    questionBank.update(question = answer)
    print (questionBank)

for i in range(questionBank.items()):
    
