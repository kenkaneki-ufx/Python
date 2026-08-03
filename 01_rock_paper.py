import random
import time
    
bot = random.choice([1,0,-1])
dash = '-'*25
print(f"{dash}\nROCK \t PAPER \t SCISSORS\n{dash}")
youin = input("Enter your choice: ")                                             # 1  for rock
dict = {"rock" : 1, "paper" : 0, "scissors" : -1,"r" : 1, "p" : 0, "s" : -1}     # 0  for paper
revdict = {1 : "rock", 0 : "paper", -1 : "scissors"}                             # -1 for scissors
you = dict.get(youin.lower())     

time.sleep(1.3)     #Optional
print(dash)         #for user interface

try:
    print(f"\tYou : {revdict[you]}\n\tBot : {revdict[bot]}")
except KeyError:
    print('Oops...Invalid input')
if (bot == you):
    print("\tIt's a Draw")
else:
    if(bot == 1 and you == 0):
        print("\tYou Win :)")
    elif(bot == 1 and you == -1):
        print("\tBot Win :(")
    elif(bot == -1 and you == 1):
        print("\tYou Win :)")
    elif(bot == -1 and you == 0):
        print("\tBot Win :(")
    elif(bot == 0 and you == -1):
        print("\tYou Win :)")
    elif(bot == 0 and you == 1):
        print("\tBot Win :(")
print(dash)