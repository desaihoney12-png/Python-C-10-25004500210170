inventory = {"Pen": 10, "Book": 4, "Pencil": 20}

def add_item(name, quantity):
    inventory[name] = quantity

def remove_item(name):
    if name in inventory:
        del inventory[name]

def update_qty(name, quantity):
    if name in inventory:
        inventory[name] = quantity

def display_inventory():
    for name, quantity in inventory.items():
        print(name, ":", quantity)

def low_stock():
    for name, quantity in inventory.items():
        if quantity < 5:
            print(name, "is low in stock")

add_item("Eraser", 3)
update_qty("Pen", 15)
remove_item("Pencil")
display_inventory()
print("Low stock items:")
low_stock()
