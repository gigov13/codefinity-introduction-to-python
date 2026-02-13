meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["mustard", 1.99, 75, "Spicy"]

deli_dept = [meat, cheese, condiment]
print(f"Initial Deli list: {deli_dept}")
if "Ham" in meat and meat[2]<100:
    meat[2] = 100
season_meat = ["Turkey", 4.50, 100, "Sliced"]

deli_dept.append (season_meat)
deli_dept.remove (condiment)
deli_dept.sort()

print(f"Updated Deli List: {deli_dept}")