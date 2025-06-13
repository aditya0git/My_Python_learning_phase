import time

questions ={
"q1": "Q1. What is the capital of India?",
"q2": "Q2. Which planet is known as the Red Planet?",
"q3": "Q3. Who wrote the national anthem of India?",
"q4": "Q4. What is the boiling point of water",
"q5": "Q5. Which is the largest ocean in the world",
"q6": "Q6. Who invented the light bulb?",
"q7": "Q7. How many continents are there on Earth?",
"q8": "Q8. Which is the national animal of India?",
"q9": "Q9. Which gas do plants absorb from the atmosphere?",
"q10": "Q10. What is the square root of 144?",
 }

options = {
"q1": "a. Mumbai\nb. Kolkata\nc. New Delhi\nd. Chennai",
"q2": "a. Earth\nb. Venus\nc. Mars\nd. Jupiter",
"q3": "a. Mahatma Gandhi\nb. Rabindranath Tagore\nc. Subhash Chandra Bose\nd. Sarojini Naidu",
"q4": "a. 90°C\nb. 95°C\nc. 100°C\nd. 110°C",
"q5": "a. Indian Ocean\nb. Atlantic Ocean\nc. Arctic Ocean\nd. Pacific Ocean",
"q6": "a. Thomas Edison\nb. Alexander Graham Bell\nc. Nikola Tesla\nd. Isaac Newton",
"q7": "a. 5\nb. 6\nc. 7\nd. 8",
"q8": "a. Elephant\nb. Tiger\nc. Lion\nd. Leopard",
"q9": "a. Carbon Dioxide\nb. Nitrogen\nc. Oxygen\nd. Hydrogen",
"q10": "a. 10\nb. 11\nc. 12\nd. 13", }


correct_options = {
"q1": "c", "q2": "c", "q3": "b", "q4": "c", "q5": "d",
"q6": "a", "q7": "c", "q8": "b", "q9": "a", "q10": "c"
}

name = input("Enter your name : ")
print("Hello!", name, "let's begin the game \"KBC\"")

time.sleep(2)
print("GAME RULES :-")
print("you will be rewarded with an amount of 1000.00 Rupees for each correct answer\nAnd will eliminated from the game on a wrong answer\n")

key = input("Enter y to start the game : ")
if key == "y" :
    start = True
else :
    start = False

if start == True :
    print("Starting your Game",end="")

    for i in range(0,10) :
        time.sleep(0.25)
        print(".", end=" ")
    print("\n")

    correct_answers = 0
    for i in questions :
        print(questions[i])
        print(options[i])


        k = 0
        eliminate = False
        u_answer = ""
        while True :   
            u_answer = input("Enter answer of your choice : ")
            if ((u_answer != "a" and u_answer != "b") and (u_answer != "c" and u_answer != "d")) :
                print("invalid input\nplease select out of a, b, c or d only")
                if k < 2 :
                    k += 1
                    continue
                else :
                    print("you have been eleminated from the game due too much of wrong entries")
                    eliminate = True
                    break
            else :
                break
        if eliminate == True :
            break


        if u_answer == correct_options[i] :
            print("   CORRECT ANSWER 👏👏👏👏 \n")
            correct_answers += 1
            time.sleep(1)
        else :
            print("       WRONG ANSWER ❌ \n")
            print("you have been eliminated from the game\n")
            break
    time.sleep(1)
    print("Game Over !!!!!\n")
    time.sleep(1)
    print("Your stats :-")
    print("you have given",correct_answers,"correct answers\nAnd you have won amount",correct_answers*1000,"INR")
