# Initial contact book
contacts = {
    "Jay": "7406302545",
    "Pree": "8867239590"
}

# Get input from user
name = input("Enter contact name: ")
phone = input("Enter phone number: ")

# Check if contact exists
if name in contacts:
    print(f"{name} already exists with number {contacts[name]}. Updating number...")
else:
    print(f"Adding new contact: {name}")

# Add or update contact
contacts[name] = phone

# Show updated contact book
print("\nUpdated Contact Book:")
for contact_name, number in contacts.items():
    print(f"{contact_name}: {number}")
