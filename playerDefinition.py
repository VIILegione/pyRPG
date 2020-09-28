import sqlite3
conn = sqlite3.connect('game.db')
c = conn.cursor()
conn.commit()


def databaseUpdate():
    try:
        global characterId
        global characterName
        global characterClass
        global characterLevel
        global characterExperience
        global characterMaxExperience
        global characterLife
        global characterArmorClass
        global characterStrength
        global characterWeaponMinDamage
        global characterWeaponMaxDamage
        global characterLifeDice
        global characterStrengthDice

        c.execute('SELECT characterId FROM characters')
        characterId = c.fetchone()
        characterId = int(''.join(map(str, characterId)))
        c.execute('SELECT characterName FROM characters')
        characterName = c.fetchone()
        characterName = str(''.join(map(str, characterName)))
        c.execute('SELECT characterClass FROM characters')
        characterClass = c.fetchone()
        characterClass = str(''.join(map(str, characterClass)))
        c.execute('SELECT characterLevel FROM characters')
        characterLevel = c.fetchone()
        characterLevel = int(''.join(map(str, characterLevel)))
        c.execute('SELECT characterExperience FROM characters')
        characterExperience = c.fetchone()
        characterExperience = int(''.join(map(str, characterExperience)))
        c.execute('SELECT characterMaxExperience FROM characters')
        characterMaxExperience = c.fetchone()
        characterMaxExperience = int(''.join(map(str, characterMaxExperience)))
        c.execute('SELECT characterLife FROM characters')
        characterLife = c.fetchone()
        characterLife = int(''.join(map(str, characterLife)))
        c.execute('SELECT characterArmorClass FROM characters')
        characterArmorClass = c.fetchone()
        characterArmorClass = int(''.join(map(str, characterArmorClass)))
        c.execute('SELECT characterStrength FROM characters')
        characterStrength = c.fetchone()
        characterStrength = int(''.join(map(str, characterStrength)))
        c.execute('SELECT characterWeaponMinDamage FROM characters')
        characterWeaponMinDamage = c.fetchone()
        characterWeaponMinDamage = int(''.join(map(str, characterWeaponMinDamage)))
        c.execute('SELECT characterWeaponMaxDamage FROM characters')
        characterWeaponMaxDamage = c.fetchone()
        characterWeaponMaxDamage = int(''.join(map(str, characterWeaponMaxDamage)))
        c.execute('SELECT characterLifeDice FROM characters')
        characterLifeDice = c.fetchone()
        characterLifeDice = int(''.join(map(str, characterLifeDice)))
        c.execute('SELECT characterStrengthDice FROM characters')
        characterStrengthDice = c.fetchone()
        characterStrengthDice = int(''.join(map(str, characterStrengthDice)))
        conn.commit()
    except:
        print("No character has been found in the database. \n Character Creation start soon...")


def databaseCreation():
    c.execute('''CREATE TABLE IF NOT EXISTS characters
                     (characterId INTEGER PRIMARY KEY AUTOINCREMENT, characterName text, characterClass text,
                      characterLevel INTEGER, characterExperience INTEGER, characterMaxExperience INTEGER,
                      characterLife INTEGER, characterStrength INTEGER, characterArmorClass INTEGER,
                      characterWeaponMinDamage INTEGER, characterWeaponMaxDamage INTEGER, characterLifeDice INTEGER,
                      characterStrengthDice INTEGER)''')
    conn.commit()
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (itemId INTEGER PRIMARY KEY AUTOINCREMENT, itemName text, itemQuantity INTEGER)''')
    conn.commit()


def raceSelector():
    input("Welcome to gamename, press enter to create a new Character")
    nameSelector = input("Write your name \n")
    selectorRace = int(input(
        "Select your class:\n"
        "1.Barbarian: This class have high strength, focused on damage\n"
        "2.Warrior: This class have high life points, focused on defence\n"))

    if selectorRace == 1:
        print("You have selected Barbarian")
        c.execute('''INSERT INTO characters (
        characterName ,characterClass, characterLife, characterArmorClass,
        characterStrength, characterLevel, characterExperience, characterMaxExperience,
        characterWeaponMinDamage, characterWeaponMaxDamage, characterLifeDice, characterStrengthDice
        ) 
        VALUES (? , 'Barbarian', '15', '14', '10', '1', '0', '200', '1', '12', '6', '4')''', (nameSelector,))
    elif selectorRace == 2:
        print("You have selected Warrior")
        c.execute('''INSERT INTO characters (
        characterName ,characterClass, characterLife, characterArmorClass, 
        characterStrength, characterLevel, characterExperience, characterMaxExperience,
        characterWeaponMinDamage, characterWeaponMaxDamage, characterLifeDice, characterStrengthDice
        ) 
         VALUES (? ,'Warrior', '30', '16', '5', '1', '0', '200', '1', '6', '12', '2')''', (nameSelector,))


def characterStats():
    print(str(
        "Character Name: " + str(characterName) + " | " + "Class: " + str(characterClass) + " | " + "Weapon: " + str(characterWeaponMinDamage) + "-" + str(characterWeaponMaxDamage) + "\n" +
        "Strength: " + str(characterStrength) + " | " + "Health: " + str(characterLife) + " | " + "Armor Class: " + str(characterArmorClass) + "\n" +
        "Current Experience: " + str(characterExperience) + " | " + "Max Experience: " + str(characterMaxExperience) + " | " + 'Level: ' + str(characterLevel) + "\n"
        ))
    databaseUpdate()
