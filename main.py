import random

fileHeroes = "heroes.txt"
fileVillains = "villains.txt"
fileWeapons = "weapons.txt"

def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.readlines()
    return data

superheroes = load_data(fileHeroes)
villains = load_data(fileVillains)
weapons = load_data(fileWeapons)

randomHero = random.choice(superheroes).strip()
randomVillain = random.choice(villains).strip()

randomWeapon = random.choice(weapons).strip()
villainWeapon = random.choice(weapons).strip()

while randomWeapon == villainWeapon:
    villainWeapon = random.choice(weapons).strip()

heroHealth = 100
villainHealth = 100

def calculate_attack(weapon):
    return len(weapon)

print(f"{randomHero} fights {randomVillain}!")
print(f"{randomHero} has a {randomWeapon}.")
print(f"{randomVillain} has a {villainWeapon}.")

while heroHealth > 0 and villainHealth > 0:

    heroAttack = calculate_attack(randomWeapon)
    villainHealth = villainHealth - heroAttack

    if villainHealth < 0:
        villainHealth = 0

    print(f"\n{randomHero} attacks with {randomWeapon}.")
    print(f"Damage: {heroAttack}")
    print(f"{randomVillain} health: {villainHealth}")

    if villainHealth == 0:
        break

    villainAttack = calculate_attack(villainWeapon)
    heroHealth = heroHealth - villainAttack

    if heroHealth < 0:
        heroHealth = 0

    print(f"\n{randomVillain} attacks with {villainWeapon}.")
    print(f"Damage: {villainAttack}")
    print(f"{randomHero} health: {heroHealth}")

if heroHealth > 0:
    print(f"\n{randomHero} saves the day!")
else:
    print(f"\n{randomVillain} wins!")
