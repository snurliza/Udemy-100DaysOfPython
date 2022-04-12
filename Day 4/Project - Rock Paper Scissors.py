import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

if player < 0 or player >= 3:
  print("You have entered invalid number, You lose!")
else:
  print(images[player])
  
  computer = random.randint(0,2)
  print(images[computer])
  
  if player == computer:
    print("It's a draw!")
  elif player == 0 and computer == 1:
    print("You lose!")
  elif player == 0 and computer == 2:
    print("You win!")
  elif player == 1 and computer == 0:
    print("You win!")
  elif player == 1 and computer == 2:
    print("You lose!")
  elif player == 2 and computer == 0:
    print("You lose!")
  elif player == 2 and computer == 1:
    print("You win!")

  
