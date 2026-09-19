import random

guess = ["Rock","Paper","Scissor"]
computer = random.choice(guess)

while True:
    user = input("Choos (r/p/s): ")
    if user == "Rock" and computer == "Paper":
        print(f"{user} win to {computer}")
        break
    elif user == "Rock" and computer == "Scissor":
        print(f"{user} win to {computer}")
        break
    elif user == "Paper" and computer == "Scissor":
        print(f"{user} loose to {computer}")
        break
    else:
        print("Enter a valid option")
