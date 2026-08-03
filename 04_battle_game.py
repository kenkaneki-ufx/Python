# A game where you fight a boss monster until someone's health hits 0.
import random
import os

def display(user_health,boss_health):
    if(user_health > 0):
        print(f"YOU :{user_health}","▬"*user_health)     #💙
    if(boss_health > 0):
        print(f"BOSS:{boss_health}","▬"*boss_health)     #💚

dash = '---------------------------------------------'
limit = range(1,20)
boss_health = 100
user_health = 100
i = -1
os.system("cls")
print(f"\n\t\tRules\n{dash}\nYour choice : 1.Attack or 2.Heal")
display(user_health,boss_health)

while (user_health > 0 and boss_health > 0):
    user_damage = random.choice(limit)
    boss_damage = random.choice(limit)
    user_heal = random.choice(limit)
    boss_heal = random.choice(limit)
    critical = random.choice(limit)
    i += 1

    if(i%2 ==0):
        user_choice = (input(f"{dash}\nEnter your choice: "))
        os.system("cls")
        if (user_choice == '1'):
            print(f"{dash}\nYour attack inflict {user_damage} damage to boss.")
            boss_health -= user_damage
        elif (user_choice == '2'):
            print(f"{dash}\nYou restored {user_heal} health")
            user_health += user_heal
        elif(user_choice == '/'):
            print(f"{dash}\nYour attack inflict {user_damage + critical} critical damage to boss.")
            boss_health -= (user_damage + critical)
        else:
            print(f"{dash}\nEnter valid choice..[1 or 2]")
            i -= 1

    else:
        if (boss_health > 45):
            boss_choice = random.choice([1,1,1,2,2,3])
        else:
            boss_choice = random.choice([2,2,2,3,3])
        if (boss_choice == 1):
            print(f"boss's attack inflict {boss_damage} damage to you.")
            user_health -= boss_damage
        elif (boss_choice == 2):
            print(f"boss restored {boss_heal} health")
            boss_health += boss_heal
        elif (boss_choice == 3):
            print(f"boss's attack inflict {boss_damage + critical} damage to you.")
            user_health -= (boss_damage + critical)
        display(user_health,boss_health)
else:
    display(user_health,boss_health)
    if(user_health <= 0):
        print(f"{dash}\nYou are dead.\nboss Wins..!\n{dash}")
    elif(boss_health <= 0):
        print(f"{dash}\nboss is dead.\nYou Wins..!\n{dash}")
