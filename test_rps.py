import random
import time
import pyttsx3
engine = pyttsx3.init()

bot = random.choice([1,0,-1])
engine.say("it's, Rock:paper:scissors")
engine.say("Enter your choice")
engine.runAndWait()

youin = input("Enter your choice: ")                                             # 1  for rock
dict = {"rock" : 1, "paper" : 0, "scissors" : -1,"r" : 1, "p" : 0, "s" : -1}     # 0  for paper
revdict = {1 : "rock", 0 : "paper", -1 : "scissors"}                             # -1 for scissors
you = dict.get(youin.lower())     
dash = '------------------------------'
time.sleep(1.3)     #Optional
print(dash)         #for user interface 

print(f"\tYou : {revdict[you]}\n\tBot : {revdict[bot]}")
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
    elif(bot == 0 and you == 1):
        print("\tYou Win :)")
    elif(bot == 0 and you == -1):
        print("\tBot Win :(")

print(dash)