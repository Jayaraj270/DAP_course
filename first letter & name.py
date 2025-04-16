# Sample list of names
names = ["Jay", "Jayaraj", "Pree", "Preethi", "Shalu", "Shalini", "Gagan","Gagan Gowda"]

# Dictionary to group names by first letter
grouped_names = {}

for name in names:
    first_letter = name[0].upper()  # Make grouping case-insensitive
    if first_letter not in grouped_names:
        grouped_names[first_letter] = []
    grouped_names[first_letter].append(name)

# Print each group on a new line
for letter, name_list in grouped_names.items():
    print(f"{letter}: {name_list}\n")
