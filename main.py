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
movements = [rock, paper, scissors]
results = ["You win!", "Computer wins!", "It's a draw."]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(user < 0 or user > 2):
  print("You typed an invalid number.")
else:
  user_movement = movements[user]
  print(user_movement)
  
  print("Computer chose:")
  computer = random.randint(0, 2)
  computer_movement = movements[computer]
  print(computer_movement)
  
  if(user == 0 and computer == 0):
    print(results[2]) # Draw
  elif(user == 0 and computer == 1):
    print(results[1]) # Computer
  elif(user == 0 and computer == 2):
    print(results[0]) # User
  
  elif(user == 1 and computer == 0):
    print(results[0]) # User
  elif(user == 1 and computer == 1):
    print(results[2]) # Draw
  elif(user == 1 and computer == 2):
    print(results[1]) # Computer
  
  elif(user == 2 and computer == 0):
    print(results[1]) # Computer
  elif(user == 2 and computer == 1):
    print(results[0]) # User
  elif(user == 2 and computer == 2):
    print(results[2]) # Draw
