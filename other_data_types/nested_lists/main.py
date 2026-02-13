vegetables = ["tomatoes", "potatoes", "onions"]
bread = ["Bread", 4.80, 3, "Gluten Free"] # Item name, price, quantity, type
milk = ["Milk", 5.99, 2, "2% Milk"]
apple = ["Apple", 1.27, 12, "Fuji"]

vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print(f"Updated Vegetable Inventory: {vegetables}")
if "carrots" in vegetables:
    print ("Carrots are already in the list")
if "cucumbers" in vegetables:
    print ("Cucumbers are already in the list")