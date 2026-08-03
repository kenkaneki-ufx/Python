# A game where you fight a boss monster until someone's health hits 0.
import random
import pyttsx3
def display(user_health,boss_health):
    print(f"YOU :{user_health}","▬"*user_health)     #💙
    print(f"BOSS:{boss_health}","▬"*boss_health)     #💚

engine = pyttsx3.init()
dash = '---------------------------------------------'
limit = range(1,20)
boss_health = 100
user_health = 100
i = -1
print(f"\n\t\tRules\n{dash}\nYour choice : 1.Attack or 2.Heal")
engine.say("RULES:,   Your choice : 1: Attack, 2: Heal.")
engine.say("Enter your choice: ")
engine.runAndWait()

while (user_health > 0 and boss_health > 0):
    user_damage = random.choice(limit)
    boss_damage = random.choice(limit)
    user_heal = random.choice(limit)
    boss_heal = random.choice(limit)
    critical = random.choice(limit)
    display(user_health,boss_health)
    i += 1

    if(i%2 ==0):
        if (user_health > 0):
            
            user_choice = (input(f"{dash}\nEnter your choice: "))
            engine.say("Enter your choice: ")
            if (user_choice == '1'):
                print(f"Your attack inflict {user_damage} damage to boss.")
                # engine.say("Your attack inflict damage to boss.")
                boss_health -= user_damage
            elif (user_choice == '2'):
                print(f"You restored {user_heal} health")
                user_health += user_heal
            elif(user_choice == '/'):
                print(f"Your attack inflict {user_damage} critical damage to boss.")
                boss_health -= (user_damage + critical)
            else:
                print("Enter valid choice..[1 or 2]")

    else:
        if (boss_health > 0):
            if (boss_health > 45):
                boss_choice = random.choice([1,1,1,2,2,3])
            else:
                boss_choice = random.choice([2,2,2,2,3])
            if (boss_choice == 1):
                print(f"boss's attack inflict {boss_damage} damage to you.")
                user_health -= boss_damage
            elif (boss_choice == 2):
                print(f"boss restored {boss_heal} health")
                boss_health += boss_heal
            elif (boss_choice == 3):
                print(f"boss's attack inflict {boss_damage} damage to you.")
                user_health -= (boss_damage + critical)

else:
    if(user_health <= 0):
        print(f"{dash}\nYou are dead.\nboss Wins..!\n{dash}")
    elif(boss_health <= 0):
        print(f"{dash}\nboss is dead.\nYou Wins..!\n{dash}")