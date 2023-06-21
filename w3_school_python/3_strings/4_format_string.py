age = 36
txt = "My name is John, and I am {}"

print(txt.format(age))

print("################################")

quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want {} pieces of item {} for {} dollars."

# I want 3 pieces of item 567 for 49.95 dollars.
print(myOrder.format(quantity, itemNo, price))

print("################################")
quantity = 3
itemNo = 567
price = 49.95
myOrder = "I want to pay {2} dollars for {0} pieces of item {1}."
# I want to pay 49.95 dollars for 3 pieces of item 567.
print(myOrder.format(quantity, itemNo, price))
