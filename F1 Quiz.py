gameState = 0
score = 0

if gameState == 0 :
    print("Welcome to Kushal's F1 Quiz!")
    print("You will be asked 10 questions about Formula 1.")
    print("Type the correct option number to win the game!")
    if input("Type Y to Start: ").lower() == "y":
        gameState = 1

if gameState == 1:
    print("=========================================================")
    print("Q1. Who won the 2020 Formula 1 World Championship?")
    print("1. Lewis Hamilton")
    print("2. Max Verstappen")
    print("3. Sebastian Vettel")
    print("4. Charles Leclerc")
    answer = input("Your answer: ")
    
    if answer == "1":
        score += 1
        print("Correct! Lewis Hamilton won the 2020 championship.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 2
        
    else:
        print("Incorrect! The correct answer is 1. Lewis Hamilton.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 2

if gameState == 2:
    print("=========================================================")
    print("Q2. Which team did Michael Schumacher drive for in his last F1 season?")
    print("1. Ferrari")
    print("2. Mercedes")
    print("3. Red Bull Racing")
    print("4. Williams")
    answer = input("Your answer: ")
    
    if answer == "1":
        score += 1
        print("Correct! Schumacher drove for Ferrari in his last season.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 3
    else:
        print("Incorrect! The correct answer is 1. Ferrari.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 3

if gameState == 3:
    print("=========================================================")
    print("Q3. What does DRS stand for in F1?")
    print("1. Driver Reaction Score")
    print("2. Downforce Reduction System")
    print("3. Drag Reduction System")
    print("4. Driver Rating System")
    answer = input("Your answer: ")
    
    if answer == "3":
        score += 1
        print("Correct! DRS stands for Drag Reduction System.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 4
    else:
        print("Incorrect! The correct answer is 3. Drag Reduction System.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 4

if gameState == 4:
    print("=========================================================")
    print("Q4. In which year did the 1st ever F1 race take place?")
    print("1. 1980")
    print("2. 1970")
    print("3. 1960")
    print("4. 1950")
    answer = input("Your answer: ")

    if answer == "4":
        score += 1
        print("Correct! The 1st ever F1 race took place in 1950.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 5
    else:
        print("Incorrect! The correct answer is 4. 1950.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 5

if gameState == 5:
    print("=========================================================")
    print("Q5. Which Flag is used to signal the end of the race?")
    print("1. Yellow Flag")
    print("2. Checkered Flag")
    print("3. Red Flag")
    print("4. Blue Flag")
    answer = input("Your answer: ")

    if answer == "2":
        score += 1
        print("Correct! The 1st ever F1 race took place in 1950.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 6
    else:
        print("Incorrect! The correct answer is 4. 1950.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 6

if gameState == 6:
    print("=========================================================")
    print("Q6. Which team is known as the “Prancing Horse”?")
    print("1. Mercedes")
    print("2. McLaren")
    print("3. Red Bull Racing")
    print("4. Ferrari")
    answer = input("Your answer: ")

    if answer == "4":
        score += 1
        print("Correct! Ferrari is known as the Prancing Horse.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 7
    else:
        print("Incorrect! The correct answer is 4. Ferrari.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 7

if gameState == 7:
    print("=========================================================")
    print("Q7. What is the fastest recorded pit stop time in F1?")
    print("1. 1.80 seconds")
    print("2. 2.05 seconds")
    print("3. 1.95 seconds")
    print("4. 1.82 seconds")
    answer = input("Your answer: ")

    if answer == "1":
        score += 1
        print("Correct! The fastest recorded pit stop time in F1 is 1.80 seconds.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 8
    else:
        print("Incorrect! The correct answer is 1. 1.80 seconds.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 8

if gameState == 8:
    print("=========================================================")
    print("Q8. Which F1 driver is famously known as the “Smooth Operator”?")
    print("1. Charles Leclerc")
    print("2. Carlos Sainz")
    print("3. Michael Schumacher")
    print("4. Lando Norris")
    answer = input("Your answer: ")

    if answer == "2":
        score += 1
        print("Correct! Carlos Sainz is famously known as the “Smooth Operator”.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 9
    else:
        print("Incorrect! The correct answer is 2. Carlos Sainz.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 9

if gameState == 9:
    print("=========================================================")
    print("Q9. How many World Championships has Max Verstappen won?")
    print("1. 1")
    print("2. 2")
    print("3. 3")
    print("4. 4")
    answer = input("Your answer: ")

    if answer == "4":
        score += 1
        print("Correct! Max Verstappen has won 4 World Championships.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 10
    else:
        print("Incorrect! The correct answer is 4. Max Verstappen.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 10

if gameState == 10:
    print("=========================================================")
    print("Q10. What country is Lewis Hamilton from?")
    print("1. United Kingdom")
    print("2. Germany")
    print("3. Brazil")
    print("4. Canada")
    answer = input("Your answer: ")

    if answer == "1":
        score += 1
        print("Correct! Lewis Hamilton is from the United Kingdom.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 11
    else:
        print("Incorrect! The correct answer is 1. United Kingdom.")
        print("Your score is now:", score)
        if input("Type Y to continue: ").lower() == "y":
            gameState = 11

if gameState == 11:
    print("=========================================================")
    print("Congratulations! You've completed the F1 Quiz!")
    print("Your final score is:", score)
    print("Thank you for playing!")
    print("Type R to restart or any other key to exit.")
    if input().lower() == "r":
        gameState = 1