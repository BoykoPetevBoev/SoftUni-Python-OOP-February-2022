from project.bakery import Bakery

bakery = Bakery("Bakery Name")

print(bakery.add_food("Cake", "Cake 1", 1.2))
print(bakery.add_food("Cake", "Cake 2", 1.4))
print(bakery.add_food("Bread", "Bread 2", 1.4))
print(bakery.add_food("Bread", "Bread 2", 1.4))

print(bakery.add_drink("Tea", "Tea 1", 2, "Brand"))
print(bakery.add_drink("Tea", "Tea 2", 4, "Brand"))
print(bakery.add_drink("Water", "Water 2", 4, "Brand"))
print(bakery.add_drink("Water", "Water 2", 4, "Brand"))