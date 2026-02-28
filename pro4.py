
# project:4= Rock, paper Scissors game
import random

rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper='''    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''


scissors='''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_img = [rock,paper,scissors]
user_choice=int(input("welcome to rock ,paper,scissors game!\n what do you choose? type o for rock, 1 for paper,2 for scissors:"))
# 0, 1, 2
if (user_choice >=0 and user_choice <=2):
    print(game_img[user_choice])

computer_choice=random.randint(0,2)
print("computer chose:")
print(game_img[computer_choice])

if (user_choice >=3 or user_choice <0):
    print("you hv enter invalid number!") 

if ( computer_choice==0 and user_choice==2):
    print("you win")

elif (user_choice==2 and computer_choice==2):
    print("you loose")

elif ( computer_choice <= user_choice):
    print("you win")

elif (computer_choice==user_choice):
    print("its a draw!")







