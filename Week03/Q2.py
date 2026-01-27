print("=" *50)
print("Question 2: Shopping cart")
print("=" * 50)

cart =["apple", "bannana", "milk", "bread",  "apple", "eggs"]

apple_count = cart.count("apple")
print("Number of Apples: ", apple_count)

milk_position = cart.index("milk")
print("Position of Milk: ", milk)

cart.remove("apple")

# Pop an item 
remove_item = cart.pop()
print("Removed item using pop: ", removed_item)

print("Is bannana in the cart?", "bannana" in cart) #**
print("Final cart: ", cart)
print()
