import random



for i in range(3):
    user_choice = input("Enter your choice (stone/paper/scissors): ").lower()
    comp_choice = random.choice(choices)
    print("Computer chose:", comp_choice)

    if user_choice == comp_choice:
        print("It's a tie!")
    elif (user_choice == "stone" and comp_choice == "scissors") or \
         (user_choice == "paper" and comp_choice == "stone") or \
         (user_choice == "scissors" and comp_choice == "paper"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        comp_score += 1

print(f"Final Score - You: {user_score}, Computer: {comp_score}")
