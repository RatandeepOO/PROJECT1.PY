""" 1 FOR SNAKE
0 FOR GUN
-1 FOR WATER"""
import random
computer = random.choice([1, 0, -1])

player_choice = input("Enter your choice : ")

dict = {"s" : 1, "w" : -1, "g" : 0}
reverse_dict = { 1 :"Snake", -1 : "Water", 0 :"Gun"}

you = dict[player_choice]
print(f"You choose {reverse_dict[you]}\nComputer choose {reverse_dict[computer]}")


if (computer == you):
    print("It's Draw!")
else:
    if(computer == 1 and you == 0):
        print("You Win!😍")
    elif(computer == 1 and you == -1):
        print("Haar Gya be tu🤣")

    elif(computer == 0 and you == 1):
        print("Haar Gya be tu🤣")
    elif(computer == 0 and you == -1):
        print("You Win!😍")

    elif(computer == -1 and you == 0):
        print("Haar Gya be tu🤣")
    elif(computer == -1 and you == 1):
        print("You Win!😍")