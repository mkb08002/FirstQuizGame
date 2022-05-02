import math


print("Welcome to my quiz game!")

answer = input("Would you like to play a game? ")

if answer.lower() == "yes":
    print("Great! Let's get started! ")
else:
    print("Come back soon!")
    quit()

score = 0

# Question 1 of 5
answer = input("Is a 50lb bag of bricks heavier than a 50lb bag of feathers? type y/n ")
if answer.lower() == "y":
    print("Think about it. 50lbs = 50lbs so they weigh the same! Better luck on the next question.")
else:
    print("Correct! Great job.")
    score += 1

# Question 2 of 5
answer = input("What is the capital of Hawaii? ")
if answer.lower() == "honolulu":
    print("Correct! Keep up the good work.")
    score += 1
else:
    print("We were looking for Honolulu. Don't worry, there are still a few questions to go.")

# Question 3 of 5
answer = input("What is 3+5? ")
if answer == "8":
    print("That was an easy one - nicely done.")
    score += 1
else:
    print("Nope it's 8. Where is your head at??")
    

# Question 4 of 5
answer = input("What is the first name of the vampire slayer of Sunnydale? ")
if answer.lower() == "buffy":
    print("Awesome job. One more question to go.")
    score += 1
else:
    print("No dice, the answer was Buffy. One more question left. You got this!")

# Question 5 of 5
answer = input("Complete this phrase: Where in the world is ------ --------? ")
if answer.lower() == "carmen sandiego":
    print("You nailed it!")
    score += 1
else:
    print("Nice try, but not quite. The correct answer is Carmen Sandiego.")

your_score = math.floor((score/5) * 100)

print("That's the end of the game! You got " + str(score) + " correct for a score of " + str(your_score) + "%!")