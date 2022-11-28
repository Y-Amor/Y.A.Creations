import time
questionNumber = 0
right = 0
wrong = 0
name = str(input("Please Enter your name "))
print()
wrongAnsweredQuestions = []
def questions():
    def questionOne():
        global right, wrong, questionNumber
        print("Who has won the most NBA Championships?")
        print("Is it A:BillRussel B:LebronJames C:MichaelJordan or D:AlexCaruso")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'BillRussel' or ans == 'Bill Russel':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("Who has won the most NBA Championships?")
        questionNumber = questionNumber + 1
    questionOne()
    time.sleep(1)
    print()
    print("So far",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(2)
    def questionTwo():
        global right, wrong, questionNumber
        print("What year was Lebron James Drafted?")
        print("Is it A:2002 B:2004 C:1999 or D:2003")
        ans = str(input())
        if ans == "D" or ans == "d" or ans == '2003'or ans == '03':
            print("You got it right!")
            right = right + 1
            
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("What year was Lebron James Drafted?")
        questionNumber = questionNumber + 1   
    questionTwo()
    time.sleep(1)
    print()
    print("So far ",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(1)
    def questionThree():
        global right, wrong, questionNumber
        print("Who was the head coach of the Golden State Warriors before Steve Kerr?")
        print("Is it A:KeithSmart B:DonNelson C:Joe Thsai or D:MarkJackson")
        ans = str(input())
        if ans == "D" or ans == "d" or ans == 'MarkJackson'or ans == 'Mark Jackson':
            print("You got it right!")
            right = right + 1
            
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("Who was the head coach of the Golden State Warriors before Steve Kerr?")
        questionNumber = questionNumber + 1   
    questionThree()
    time.sleep(1)
    print()
    print("So far ",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(1)
    def questionFour():
        global right, wrong, questionNumber
        print("What team drafted Kobe Bryant?")
        print("Is it A:Charlotte Hornets  B:Charlotte Bobcats C:Los-Angles Lakers or D: Clevland Cavaliers")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'Charlotte Hornets'or ans == 'CharlotteHornets':
            print("You got it right!")
            right = right + 1
        else: 
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("What team drafted Kobe Bryant?")
        questionNumber = questionNumber + 1   
    questionFour()
    
    def questionFive():
        global right, wrong, questionNumber
        print("Which team has won the most regular season games in a single season?")
        print("Is it A:Chicago Bulls  B:Los Angles Lakers  C:Golden State Warriors or D:New York Knicks")
        ans = str(input())
        if ans == "C" or ans == "c" or ans == 'Golden State Warriors' or ans == 'GoldenStateWarriors':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("Which team has won the most regular season games in a single season?")
        questionNumber = questionNumber + 1
    questionFive()
    time.sleep(1)
    print()
    print("So far",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(1)
    
    def questionSix():
        global right, wrong, questionNumber
        print("Who is the tallest player to ever play in the NBA")
        print("Is it A:Sun Mingming  B:Yao Ming  C:Shaq or D:=Tacko Fall")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'Sun Mingming' or ans == 'SunMingming':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("Who is the tallest player to ever play in the NBA")
        questionNumber = questionNumber + 1
    questionSix()
    time.sleep(1)
    print()
    print("So far",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(1)
    
    def questionSeven():
        global right, wrong, questionNumber
        print("Who is the Tallest Player in the NBA?")
        print("Is it A:Sun Mingming  B:Yao Ming  C:Shaq or D:=Tacko Fall")
        ans = str(input())
        if ans == "A" or ans == "a" or ans == 'Sun Mingming' or ans == 'SunMingming':
            print("You got it right!")
            right = right + 1
        else:
            print("You got it wrong!")
            wrong = wrong+1
            wrongAnsweredQuestions.append("Who is the Tallest Player in the NBA?")
        questionNumber = questionNumber + 1
    questionSeven()
    time.sleep(1)
    print()
    print("So far",name,"You have got",right,"Answers right,",wrong,"Answers wrong and you have completed",questionNumber,"Questions")
    print()
    time.sleep(1)
    #classmethod

    


    def scoreCalculator():
        global right, wrong, questionNumber
        scoreGrade = right/wrong
        if (scoreGrade <= 59):
            print (name + " " + "Your grade on this quiz was an F, maybe sports isn't your thing....")
        if (scoreGrade <= 69 and scoreGrade > 59):
            print (name + " " + "Your grade on this quiz was an D, not a sports fan in my book.")
        if (scoreGrade <= 79 and scoreGrade > 69):
            print (name + " " + "Your grade on this quiz was an C, ur a Casual fan I guess ")
        if (scoreGrade <= 89 and scoreGrade > 79):
            print (name + " " + "Your grade on this quiz was an B, Way to go next time eat breakfast and you might get an A....")
        if (scoreGrade <= 99 and scoreGrade > 89):
            print (name + " " + "Your grade on this quiz was an A, Congrats ur a real fan of the NBA")
        if (scoreGrade == 100):
            print (name + " " + "You.. you.. got a perfect score... Did you use goodle??! If not wow your insane!")
        elif (scoreGrade != 100):
            c = 1
            print("Here are the Questions you missed you should probably study them but what do I know im just a computer ")
            while (c < 8):
                print(wrongAnsweredQuestions [c])
                c += 1



    scoreCalculator()



    
questions()
