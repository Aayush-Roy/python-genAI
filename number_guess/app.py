import random
random_num = random.randint(1,100)
while True:
    
    number = int(input("Guess the number between 1 to 100 "))
    if(number == random_num):
        print(f"You guess the correct number")
        break
    elif number > random_num:
        print("Too High")
    elif number < random_num:
        print("Too Low")
    else:
        print("Enter a valid Number")
    
