import sqlite3
conn = sqlite3.connect('game.db')
c = conn.cursor()


def backToMenu():
    input("Press enter to return in the main menu \n")
    start()


def addItem():
    inputItemName = input('What items do you want? \n')
    inputItemQuantity = input('Write the quantity \n')
    c.execute('''INSERT INTO ITEMS (itemName, itemQuantity) VALUES
              (?, ?)''', (inputItemName, inputItemQuantity))
    print(inputItemName + " was added in inventory with " + inputItemQuantity + " quantity")
    conn.commit()
    backToMenu()


def deleteItem():
    print(itemList)
    inputDeleteItemId = input("What item do you want to drop? write id or name \n")
    c.execute('''DELETE FROM items where itemName LIKE ? OR itemId = ? ''', (inputDeleteItemId, inputDeleteItemId,))
    print("You have dropped " + inputDeleteItemId)
    backToMenu()


def checkInventory():
    print("This is your inventory \n"
          "itemId, itemName, itemQuantity")
    c.execute('SELECT * FROM items')
    currentyItems = c.fetchall()
    global itemList
    for itemList in currentyItems:
        print(itemList)
    conn.commit()
    backToMenu()


def start():
    selector = input("Welcome to VIILegione inventory system, insert the number of what you want to execute: \n"
                     
                     "1. Check Inventory \n"
                     "2. Add Item \n"
                     "3. Delete item \n"

                     )

    if selector == "1":
        print("You have selected Check Inventory \n")
        checkInventory()
    elif selector == "2":
        print("You have selected Add Item \n")
        addItem()
    elif selector == "3":
        print("You have selected Delete Item \n")
        deleteItem()


conn.commit()
conn.close()
