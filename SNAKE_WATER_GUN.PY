import random

# Mapping choices
choice_dict = {
    "s": 1, "snake": 1,
    "w": -1, "water": -1,
    "g": 0, "gun": 0
}
reverse_dict = {1: "Snake", -1: "Water", 0: "Gun"}

print("Welcome to Snake-Water-Gun Game!")
print("Type 'snake' or 's', 'water' or 'w', 'gun' or 'g'. Type 'q' to quit.")

while True:
    player_input = input("\nEnter your choice: ").lower()
    
    if player_input == 'q':
        print("Thanks for playing!")
        break
    
    if player_input not in choice_dict:
        print("Invalid choice. Try again.")
        continue
    
    player_choice = choice_dict[player_input]
    computer_choice = random.choice([1, 0, -1])
    
    print(f"You chose: {reverse_dict[player_choice]}")
    print(f"Computer chose: {reverse_dict[computer_choice]}")
    
    if player_choice == computer_choice:
        print("It's a Draw!")
    elif (player_choice == 1 and computer_choice == -1) or \
         (player_choice == -1 and computer_choice == 0) or \
         (player_choice == 0 and computer_choice == 1):
        print("You Win! 😍")
    else:
        print("You Lose! 🤣")
