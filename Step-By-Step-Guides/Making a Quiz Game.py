import random #allows for the order of the questions to be randomised later on

print("Welcome to Q-Quiz!\nGood luck")

score=0

while True:
    answer=input("Ready?")
    if answer.lower()=='yes': # .lower removes any capitalisation issues with user input vs sought input       
        print("Great!")
        break
    else: 
        print("See you later!")
        continue

#input range of questions with corresponding answers
QUESTIONS = [
    ('#question1', '#answer1'),
    ('#question2', '#answer2'),
    ('#question3', '#answer3'),
]

#radomise question order
num_questions=len(QUESTIONS)
questions = random.sample(list(QUESTIONS), k = num_questions)
num = random.randint(0,num_questions)
CORRECT = [
    "#output1",
    "#output2",
    "#output3",
]

INCORRECT = [
    "#output1",
    "#output2",
    "#output3",
]

#provide a score for the whole quiz to the user

correct_answer = CORRECT[num]
incorrect_answer = INCORRECT[num]

for question, right_answer in questions:
    answer = input(f"{question}")
    if answer.lower() != right_answer:
        print(incorrect_answer)
        continue
    score += 1
    print(correct_answer)

#end the quiz
print("⭐ Congratulations! You've made it! ⭐\nYou answered",score,"questions correctly!")
mark=(score/num_questions)*100
print('Total marks:',mark)
print('Thank you for playing, I hope you had fun!')
exit()
