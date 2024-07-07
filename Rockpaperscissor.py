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
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
'''print(rock)
print(paper)
print(scissor)'''
game_image = [rock,paper,scissor]
for idx in range(0,len(game_image)):
    print(game_image[idx])


user_choice = int(input("""What do you choose? From below:
        1)type 0 for rock
        2)type 1 for paper 
        3)type 2 for scissor\n
        Enter Choice:   """))
 # 0 -> rock , 1-> paper 2 -> scissor
if user_choice >= 3 or user_choice < 0:
    print("You Entered Invalid choice, so you loose!")
else:

    print(game_image[user_choice])
    computer_choice = random.randint(0,2)
    print("Computer choose:")
    print(game_image[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose!")   
    elif computer_choice > user_choice:
        print("You loose!")
    elif user_choice > computer_choice:
        print("You win!")   
    elif computer_choice == user_choice:
        print("It's draw!")

