#This is a python script that simulates a Rock Paper Scissors 
#with user input and the CPU making a random choice. The game is 
#intended to help with understanding conditional logic in the
#Python language.
#Author: Ja'Quis Franklin
#Date: 02/10/2025
import random

#Function to allow the computer to simulate an opponent
#Choosing between the options
def cpu_Choice():
    choices = ["Rock", "Paper", "Scissors"]
    choice = random.choice(choices)
    return choice

print("Let's Play Rock, Paper Scissors")
print("[R]ock")
print("[P]aper")
print("[S]cissors\n")

done = False
while not done:
    userChoice = input(str("SHOOT: "))

    match userChoice.lower().strip():
            case "r":
                userChoice = "Rock"
            case "p":
                userChoice = "Paper"
            case "s":
                userChoice = "Scissors"
            case _:
                print("Invalid. Choose Again:")
                continue

    cpuChoice = cpu_Choice()
    print(f"CPU chose: {cpuChoice}\n") 
    if userChoice == cpuChoice:
     print("Game Tied. Go Again!")
    elif (userChoice == "Rock" and cpuChoice == "Paper") or\
        (userChoice == "Scissors" and cpuChoice == "Rock") or\
        (userChoice == "Paper" and cpuChoice == "Scissors"):
        print("You Lose.")
        done = True
    else:
        print("YOU WIN!!")
        done = True