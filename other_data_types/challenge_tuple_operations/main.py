# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print("Number of Apples: ", apple_count)

banana_index = shelf.index ("bananas")
print("First banana Index: ", banana_index)

if shelf.count ("apples") < 5:
    print("Apples need to be restocked.")
elif shelf.count("apples")>= 5: 
    print("Apples are sufficient stocked.")

if shelf.count("grapes") == 1:
    print ("Grapes need to be restocked.")
elif shelf.count("grapes") != 1:
    print("Grapes are sufficiently stocked.")
orrange_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index: ", orrange_index )
else: print("Oranges are out of stock.")