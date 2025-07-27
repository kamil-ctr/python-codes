import random
import time

player_health = 100
dragon_health = 100

def dragon_attack():
    return random.randint(5, 30)

def player_attack():
    return random.randint(15, 30)

def player_defend(damage):
    return damage // 2

def dragon_defend(damage):
    return damage // 1.5

def print_slow(str):
    for char in str:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

print_slow("Welcome to the Dragon Tower Game!")

while player_health > 0 and dragon_health > 0:
    print("\nPlayer health:", player_health)
    print("Dragon health:", dragon_health)
    print("\nIt's your turn:")
    print("1. Attack")
    print("2. Defend")
    choice = input("Choose your move (1 or 2): ")
    
    if choice == "1":
        damage_to_dragon = player_attack()
        dragon_health -= damage_to_dragon
        player_health -= dragon_attack() 
        print_slow("You attack the dragon and deal " + str(damage_to_dragon) + " damage!")
        print_slow("Dragon has attacked you and dealt :"+ str(dragon_attack())+"damage")
    elif choice == "2":
        dragon_damage = dragon_attack()
        player_health -= player_defend(dragon_damage)
        player_damage = player_attack()
        dragon_health-= dragon_defend(player_damage)
        print_slow("You defend against the dragon's attack and take " + str(player_defend(dragon_damage)) + " damage!")
        print_slow("You counter succesfully and dealt "+str(player_damage)+"damage." )
    else:
        print_slow("Invalid choice. Try again!")
        continue

    if player_health <= 0:
        print_slow("You have been defeated by the dragon. Game Over!")
    elif dragon_health <= 0:
        print_slow("Congratulations! You have defeated the dragon!")
    else:
        print_slow("Next round!\n")
print("Thanks for playing!")