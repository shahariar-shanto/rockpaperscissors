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








user_input= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

B= [rock, paper, scissors]
B= B[user_input]
print(B)



import random

A= [rock, paper, scissors]

number= random.randint(0,2)

print(A[number])

A= A[number]


if B==A:
    print("Draw Match, Both are same ")
    
if B==rock and A==paper:
    print("You Lose, Paper is powerfull")
    
if B==paper and A==rock:
    print("You Win, Paper is powerfull")

if B==rock and A==scissors:
    print("Rock breaks Scissors, You Win")
    
if B==paper and A==scissors:
    print("Scissors cuts paper, You lose")
    
if B==scissors and A==paper:
    print("you win")
    
if B==scissors and A==rock:
    print(" Rock breaks Scissors, You lose")


