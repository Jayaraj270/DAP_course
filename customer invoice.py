customer_name = input("Enter customer name: ")
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

print("\n----- INVOICE -----")
print("Customer:", customer_name)
print("Product:", product)
print("Quantity:", quantity)
print("Price per item: ₹", price)
print("Total: ₹", total)
print("-------------------")
