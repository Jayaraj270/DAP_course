colors = ['red', 'green', 'white', 'black']

print("Traversing the list in reverse order with original indices:\n")

for i in range(len(colors) - 1, -1, -1):
    print(f"Index {i}: {colors[i]}")
