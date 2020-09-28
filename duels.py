import random
import playerDefinition
import enemy
import sqlite3
conn = sqlite3.connect('game.db')
c = conn.cursor()


class Player:
    def __init__(self, name, health, armorClass, damage, weaponMinDamage, weaponMaxDamage):
        self.name = name
        self.health = health
        self.armorClass = armorClass
        self.damage = damage
        self.weaponMinDamage = weaponMinDamage
        self.weaponMaxDamage = weaponMaxDamage


def duel():
    playerDefinition.databaseUpdate()
    global p1
    global p2
    p1 = Player(
        str(playerDefinition.characterName), int(playerDefinition.characterLife),
        int(playerDefinition.characterArmorClass), int(playerDefinition.characterStrength),
        int(playerDefinition.characterWeaponMinDamage), int(playerDefinition.characterWeaponMaxDamage)
    )

    p2 = random.choice(enemy.enemyList)

    round = 0

    print(
        p1.name + " stats: health " +
        str(p1.health) + ", damage " +
        str(p1.damage) + ", ArmorClass " +
        str(p1.armorClass)
    )

    for x in range(30):
        round = round + 1
        input("Press enter to start the round " + str(round) + "\n")
        p1.hitModifier = p1.damage / 2
        p1.hitRandom = random.randint(1, 20)
        p1.hit = p1.hitRandom + p1.hitModifier

        print(
            str(p1.name) + " try to hit " + str(p2.name) +
            " and roll " + str(p1.hitRandom) + " + strength modifier " + str(p1.hitModifier) +
            " total hit rate: " + str(p1.hit) +
            " vs " + str(p2.armorClass) + " armor class"
        )

        p2.hitModifier = p2.damage / 2
        p2.hitRandom = random.randint(1, 20)
        p2.hit = p2.hitRandom + p2.hitModifier

        print(
            str(p2.name) + " try to hit " + str(p1.name) +
            " and roll " + str(p2.hitRandom) + " + strength modifier " + str(p2.hitModifier) +
            " total hit rate: " + str(p2.hit) +
            " vs " + str(p1.armorClass) + " armor class"
        )

        if p1.hit >= p2.armorClass:
            p1.damageTotal = p1.damage / 2 + random.randint(p1.weaponMinDamage, p1.weaponMaxDamage)
            print(p2.name + " get hit by " + p1.name + " and receive " + str(p1.damageTotal) + " damage")
            p2.health = p2.health - p1.damageTotal
        else:
            print(str(p1.name) + " doesn't hit p2 " + str(p2.name))

        if p2.hit >= p1.armorClass:
            p2.damageTotal = p2.damage / 2 + random.randint(p2.weaponMinDamage, p2.weaponMaxDamage)
            p1.health = p1.health - p2.damageTotal
            print(p1.name + " get hit by " + p2.name + " and receive " + str(p2.damageTotal) + " damage")
        else:
            print(str(p2.name) + " doesn't hit " + str(p1.name))

        if p2.health <= 0:
            print(str(p2.name) + " is dead, " + str(p1.name) + " win this hunt and gain " + str(p2.experienceAmount) + " Experience")
            giveExperience()
            levelUpCheck()
            input("Press enter to go back in your shelter.")
            duelShelter()
            break

        if p1.health <= 0:
            print(str(p1.name) + " is heavy wounded, a wayfarer dragged you into your shelter.")
            duelShelter()
            break


def duelShelter():
    selectorShelter = input("\nWelcome to your shelter " + playerDefinition.characterName + ", here you can rest and recover Health, select number input option:\n"
                            "1.Start Hunt\n"
                            "2.Character Stats\n"
                            "3.Exit\n")
    if selectorShelter == "1":
        duel()
    elif selectorShelter == "2":
        playerDefinition.characterStats()
        input("Press enter to go back to shelter menu \n")
        duelShelter()
    elif selectorShelter == "3":
        selectorExit = input("You have selected 'exit', are you sure? Select number input option:\n"
                             "1.Yes\n"
                             "2.No\n")
        if selectorExit == "1":
            print("Closing game...")
            exit()
        elif selectorExit == "2":
            print("Back to shelter menu...")
            duelShelter()
        elif selectorExit != "1" or "2":
            print("Please select correct input number")
            duelShelter()
    elif selectorShelter == "":
        print("Write correct number input")
        duelShelter()
    elif selectorShelter != "1" or "2":
        print("Write correct number input")
        duelShelter()


def giveExperience():
    c.execute('UPDATE characters SET characterExperience = characterExperience +100 WHERE characterId = 1')
    conn.commit()


def levelUpCheck():
    playerDefinition.databaseUpdate()
    if playerDefinition.characterExperience >= playerDefinition.characterMaxExperience:
        c.execute('''UPDATE characters SET characterExperience = 0, characterMaxExperience = characterMaxExperience*2,
                   characterLevel = characterLevel +1, characterLife = characterLife + characterLifeDice, 
                   characterStrength = characterStrength + characterStrengthDice WHERE characterId = 1''')
        conn.commit()
        playerDefinition.databaseUpdate()
        print("LEVEL UP! Your current level is: " + str(playerDefinition.characterLevel))
