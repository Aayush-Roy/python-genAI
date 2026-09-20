import random

choice_emojis = {
    'r': '👊',
    'p': '✋',
    's': '✂️'
}

while True:
    computer_choice = random.choice(("r", "p", "s"))

    user_choice = input("Enter your choice (r/p/s): ")

    if (
        (user_choice == "r" and computer_choice == "s")
        or
        (user_choice == "s" and computer_choice == "p")
        or
        (user_choice == "p" and computer_choice == "r")
    ):
        print("User won")
    elif user_choice == computer_choice:
        print("Draw")
    else:
        print("Computer won")

    print(f"User choice: {choice_emojis[user_choice]}")
    print(f"Computer choice: {choice_emojis[computer_choice]}")

    break