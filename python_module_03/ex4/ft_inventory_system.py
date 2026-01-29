import sys

def parser(inventory, args):
    for arg in args:
        name, quantity = arg.split(':')
        inventory[name] = int(quantity)
    
def count_items(inventory):
    total = 0
    inventory_values = inventory.values()
    for v in inventory_values:
        total += v
    return total

def most_abundant(inventory):
    max_quantity = 0
    max_item = ""
    for item, quantity in inventory.items():
        if quantity > max_quantity:
            max_quantity = quantity
            max_item = item
    return max_item, max_quantity

def least_abundant(inventory, min_quantity):
    min_item = ""
    for item, quantity in inventory.items():
        if quantity < min_quantity:
            min_quantity = quantity
            min_item = item
    return min_item, min_quantity

def sort_and_display(inventory, total):
    sorted = dict()

    while len(sorted) < len(inventory):
        max_quantity = 0
        max_item = ""
        for item, quantity in inventory.items():
            if item not in sorted and quantity > max_quantity:
                max_quantity = quantity
                max_item = item
        
        print(f"{max_item}: {max_quantity} {"unit" if max_quantity == 1 else "units"} ({(max_quantity / total * 100):.1f}%)")
        sorted[max_item] = True

def item_categories(inventory):
    moderate = dict()
    scarce = dict()
    for item, quantity in inventory.items():
        if quantity < 5:
            scarce[item] = quantity
        else:
            moderate[item] = quantity
    return moderate, scarce

def restock_info(inventory):
    restock_needed = []
    for item, quantity in inventory.items():
        if quantity == 1:
            restock_needed.append(item)
    return restock_needed

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inventory = dict()
    parser(inventory, args)
    total = count_items(inventory)
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(args)}\n")

    print("=== Current Inventory ===")
    sort_and_display(inventory, total)

    print("\n=== Inventory Statistics ===")
    max_item, max_quantity = most_abundant(inventory)
    print(f"Most abundant: {max_item} ({max_quantity} {"unit" if max_quantity == 1 else "units"})")
    min_item, min_quantity = least_abundant(inventory, max_quantity)
    print(f"Least abundant: {min_item} ({min_quantity} {"unit" if min_quantity == 1 else "units"})")

    print("\n=== Item Categories ===")
    moderate, scarce = item_categories(inventory)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    print(f"Restock needed: {restock_info(scarce)}")

    print("\n=== Dictionary Properties demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    print(f"Sample lookup - 'sword' in inventory: {"sword" in inventory}")