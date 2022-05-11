#ROCK PAPER SCISSORS GAME
import random
#  Rock
rock=("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper=("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissor=("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

Game_Images=[rock,paper,scissor]
user_choice=int(input("What is yoyur choice! 0 for Rock,1 for Paper,2 for Scissor\n"))
if (user_choice>=3 or user_choice<0):
    print("you choose a invalid no. So You Loose!")
else:
    print(Game_Images[user_choice])
    
    computer_choice=random.randint(0,2)
    print("computer choose:")
    print(Game_Images[computer_choice])

    if computer_choice==user_choice:
        print("it's a draw or tya!")
    
    elif (computer_choice==0 and user_choice==2):
        print("You Loose!")
    elif(computer_choice==2 and user_choice==1):
        print("You Loose!")
    elif(computer_choice>user_choice) :
        print("You Win!")       
    elif(computer_choice<user_choice):
        print("You Win!")
    else:
        print("wrong entry")    
        