import random
from collections import defaultdict

def give_smart_hint(secrect_number):
    if(secrect_number%2 == 0):
        print("The number is: EVEN.")
    else:
        print("The number is: ODD.")

def check_guess(secrect_number,user_guess,attempt_left):
    if (secrect_number < int(user_guess)):       # High
        print(f"Too high. {attempt_left} attempts left\nTry again...!\n{dash}")
    elif (secrect_number > int(user_guess)):     # Low
        print(f"Too low. {attempt_left} attempts left\nTry again...!\n{dash}")


dash = "-"*38
attempt = 1
diff_dict = defaultdict(int)                                    #[ For Preventing INPUT ERROR]
attempt_dict = defaultdict(int)                          
diff_dict.update({"easy":10, "mid":50, "hard":100})
attempt_dict.update({"easy":10, "mid":15, "hard":20 })

print(f"\t\t   Rules:\n{dash}{dash}\nDifficulty - {diff_dict}\nAttempts - {attempt_dict}\nFor Smart [HINT] - press ENTER <-\n{dash}{dash}")
diff = input("\nEnter the difficulty level: ")
if diff in ['easy','mid','hard']:
    num = random.choice(range(diff_dict[diff]+1))

    while (attempt > 0):
        attempt_left = attempt_dict[diff] - attempt
        
        if (attempt_left < 0):          
            print("Aww...Can't guess the number\nToo bad..Looks like you are out of attempts")
            break
        
        you = input(f"{dash}\nGuess the number: ")
        if (you == ''):                
            give_smart_hint(num)        # [ HINT ]

        elif (num != int(you)):
            attempt += 1                
            check_guess(num,you,attempt_left)               # [ CHECK ]

        else:
            print(f"{dash}\nYou guessed the number in {attempt} attemps.\nCongratulation...the number was {num}\n{dash}")
            break
else:
    print("Invalid difficulty..")
