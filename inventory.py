# Sample inventory dictionary
inventory = {
    "mobile": 10,
    "laptop": 15,
    "mouse": 12
}

# Get input from user
item = input("Enter the item name to sell: ").lower()
quantity = int(input("Enter the quantity to sell: "))

# Check if the item exists in inventory
if item in inventory:
    if inventory[item] >= quantity:
        inventory[item] -= quantity
        print(f"Sold {quantity} {item}(s). Remaining stock: {inventory[item]}")
    else:
        print(f"Not enough {item}s in stock. Only {inventory[item]} available.")
else:
    print(f"Item '{item}' not found in inventory.")

# updated inventory
print("\nUpdated Inventory:")
for i, q in inventory.items():
    print(f"{i.capitalize()}: {q}")
