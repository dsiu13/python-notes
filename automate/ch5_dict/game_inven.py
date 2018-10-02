# Fantasy Game Inventory

bags = {'bandages': 12,
        'gold': 8123442,
        'health potions': 0,
        'mana potions': 8,
        'thunderfury, blessed blade of the windseeker': 1,
        'sorting hat': 1,
        'lidless wall': 1 }

def inventory(bags):
    print("In your bags: ")
    total_items = 0
    for k, v in bags.items():
        print(k + ": " + str(v))
        total_items += v
    print("total supplies: " + str(total_items))

# List to Dictionary Function for Fantasy Game Inventory
loots = ['diamond', 'ruby', 'dragon egg', 'dragon scale', 'dragon fang', 'dragon scale']

def looting(bags, lootedItems):
    for i in range(len(bags) - 1):
        print(i)
        bags[i] = loots[i]
    print(bags)

looting(bags, loots)
