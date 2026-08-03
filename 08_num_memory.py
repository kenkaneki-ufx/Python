import random


while True:
    bot = random.choice(range(1,7))
    choice = input("Choose Odd or Even:").strip().lower()
    try:
        you = int(input("Enter a number (1-6):"))
    except ValueError:
        print("Invalid input..Start again")
        break

    if you+bot %2!=0:
        toss = 'odd'
    else:
        toss = 'even'
    if toss == choice:
        game = int(input("You won the toss!\n1.Bating    2.Bowling:"))
        if game == 1:
            print("You chose Batting.")
            
    else:
        game = random.choice([1,2])
        if game == 1:
            print("Computer chose Batting.")