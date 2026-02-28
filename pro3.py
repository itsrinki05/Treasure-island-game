print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print('welcome to the treasure island ' \
'your mission is to find the treasure !')

direction=input('you\'re at a crossboad,' \
' where do you want to go? type'
' "left" or "right". ').lower()

if ( direction=="left"):
   direction2=input('you\'ve come to the lake, ' \
   'there is an island in the middle of the lake. type ' \
    '"wait" : wait for a boat , type "swim": to swim accross:').lower()
   if (direction2 == "wait"):
      direction3 = input("you arrived at the island unharmed."
                          "There is a house with three doors."
                           "one red, one blue, one yellow."
                             "which colour do you choose?").lower()
      if (direction3=="red"):
          print("it is a room of full of fire. game over!")
      elif ( direction3=="yellow"):
          print("you found the treasure . you win!")
      elif( direction3=="blue"):
          print("you enter a room of beasts. game over!")
      else:
          print("you've choose the door that is doesn't exist!")
   else:
        print("you got attacked by the angry trout. game over!")
else:
    print(" you fall into a hole:game over")




    
