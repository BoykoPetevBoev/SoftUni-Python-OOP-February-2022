from project.baked_food.cake import Cake
from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

class Bakery():
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0
    

    @property
    def name(self):
            return self.__name
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value


    def add_food(self, food_type: str, name: str, price: float):
        if any(food.name == name for food in self.food_menu):
             return f"{food_type} {name} is already in the menu!"

        if food_type == "Cake":
             self.food_menu.append(Cake(name, price))
        elif food_type == "Bread":
             self.food_menu.append(Bread(name, price))

        return f"Added {name} ({food_type}) to the food menu"


    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if any(drink.name == name for drink in self.drinks_menu):
             return f"{drink_type} {name} is already in the menu!"

        if drink_type == "Tea":
             self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
             self.drinks_menu.append(Water(name, portion, brand))

        return f"Added {name} ({drink_type}) to the food menu"


    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
             self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
             self.tables_repository.append(OutsideTable(table_number, capacity))


    def reserve_table(self, number_of_people: int):
        table = next((table for table in self.tables_repository if not table.isReserved and table.capacity >= number_of_people), None)

        if table:
             table.isReserved = True
             return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
             return f"No available table for {number_of_people} people"


    def order_food (self, table_number: int, food_name1: str, food_name2: str):
        table = next((table for table in self.tables_repository if table.table_number == table_number), None)
        
    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv" 