


while True:
    import random


    question1 = 'Question:1 > Machine language is a high level language '
    question2 = 'Question:2 > Amazon is a product based company '
    question3 = 'Question:3 > Capital of India is New Delhi '
    question4 = 'Question:4 > Only For loop is there in Python '
    question5 = 'Question:5 > LPU is located in Punjab '
    question6 = 'Question:6 > HDD is faster than SSD '
    question7 = 'Question:7 > D Drive can be created through logical partitioning '
    question8 = 'Question:8 > Capital of South Korea is not Seoul '
    question9 = 'Question:9 > Apple is an american company '
    question10 = 'Question:10 > Dr. S J Shankar is current External Affairs Minister '

    d = {question1: "False", question2: "True", question3: "True", question4: "False", question5: "True",
         question6: "False", question7: "True", question8: "False", question9: "True", question10: "True"}

    score = 0

    print()
    print("Welcome to the game of True/False Quiz, User")
    a = input("Would you like to play the game: (Y/N) ")
    b = a.title()
    if b == "N":
        quit()

    print(" Great  \n Answer the following questions \n You need 30 points to win")
    print("The Quiz will start shortly")

    for i in range(1, 6):
        random_question = random.choice(list(d))
        print("-------------------------------------------------------------------------------------------------")

        print(random_question)

        if random_question in question1:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question1)
            if x == y:
                print(" Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time")
                score = score


        elif random_question in question2:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question2)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score


        elif random_question in question3:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question3)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question4:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question4)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score


        elif random_question in question5:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question5)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question6:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question6)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question7:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question7)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question8:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question8)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question9:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question9)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score

        elif random_question in question10:
            x = input("Answer the statement, User!: ")
            x = x.title()
            y = d.get(question10)
            if x == y:
                print("Great!, keep going ")
                score = score + 10
            else:
                print("Better luck next time, keep going")
                score = score
    print("-------------------------------------------------------------------------------------------------")
    if score>20:
        print("Congratulations!!! User you cleared the test")
    else:
        print("Dont worry User, try harder next time")
    print("User your final score is : ", score)
    print("Your points in percentage are: ",((score/50)*100),"%")
