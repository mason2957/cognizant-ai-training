# creating an inventory management system
## create the inventory dictionary

inventory = {
    'Apple' : (10, 2.5),
    'Banana' : (20, 1.5),
}
print('Original: ',inventory)

inventory["Grapes"] = (30, 2.0) ## add grapes to the inventory
print('Addition: ', inventory)

del inventory["Banana"] ## delete the banana
print('Removal: ', inventory)

inventory['Apple'] = (20, 2.5) ## change the apples cost and quantity
print('Change: ', inventory)

def show_inventory(): ## Creates a function to break down each item, its quantity, and its price
    for k in inventory:
        quantity, price = inventory[k]
        print(f'Item: {k}, Quantity: {quantity}, Price: ${price}')

show_inventory()

def total_inventory(): ## creates a function to tell the total value of the inventory
    total = 0
    for k in inventory:
        quantity, price = inventory[k]
        total += price * quantity
    print(f'Total Inventory Value: ${total}')

total_inventory()

