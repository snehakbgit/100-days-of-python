import random

Rock = ('''
     _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

 ''')



Paper= (''' 
     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

''')

Scissor= (''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

''')

random_game=random.randint(0,2)
# print(random_game)

if random_game==0:
    print(Rock)
elif random_game==1:
    print(Paper)
else:
    print(Scissor)
