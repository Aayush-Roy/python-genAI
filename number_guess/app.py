import random
random_num = random.randint(1,100)
while True:
    try:
        number = int(input("Guess the number between 1 to 100 "))
    
        if number > random_num:
            print("Too High")
        elif number < random_num:
            print("Too Low")
        else:
            print("congrats u guess the correct number")
    except ValueError:
        print("Enter a valid value")    
