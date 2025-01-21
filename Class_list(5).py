
class Inventory_Management():
    def __init__(self):
        self.inventory=[]
        
    def add_item(self):
        self.name_item=input("Please Enter the item name: ")
        self.price_item=float(input("Enter The price of the item: "))
        self.quantity_item=int(input("Enter the quantity: "))
        item = [self.name_item, self.price_item, self.quantity_item]
        self.inventory.append(item)  # Append the item to the inventory as a sublist
        return item  # Return the sublist (item details)
    
    def remove_item(self):
        print(f"Your Inventory is {self.inventory}")
        remove_item=input(f"What would you like remove from the list: ")
        for item in self.inventory:
            if item[0]==remove_item:
                self.inventory.remove(item)
                print(f"Removed {remove_item} from the inventory.")
                return item
        print(f"{remove_item} is not in the inventory!")
        
    def update_item_quantity(self):
        name_item_=input("Whats the of the item you want to update: ")
        for item in self.inventory:
            if item[0]==name_item_:
                new_quantity = int(input(f"Enter the new quantity for {name_item_}: "))
                item[2] = new_quantity  
                print(f"New quantity for {name_item_} is {item[2]}")
                return
        print(f"Item {name_item_} is not in the inventory!")
            
            
    def view_inventory(self):
        print(f"Your Inventory is {self.inventory}")
        
    def search_item(self):
        item_search=input("Whats the item your looking for?: ")
        for item in self.inventory:
            if item[0] == item_search:
                print(f"{item_search} is found! The price of the item is {item[1]} and the quantity is {item[2]}")
                return
            print(f"{item_search} is not in the inventory!")
            
    def calculate_inventory(self):
        if not  self.inventory:
            print("The inventory is empty!")
            return
        total_value = 0
        for item in self.inventory:
            total_value += item[1] * item[2]  
        print(f"Total inventory value is: ${total_value:.2f}")

can_inventory=Inventory_Management()

        
while True:
    system_=input("Welcome to the Inventory Management!\n"
                  "1-Add Item \n"
                  "2-Remove Iten \n"
                  "3- View all Item \n"
                  "4- Search for a item \n"
                  "5- Calculate Inventory \n"
                  "6-Exit \n"
                  
                  ).lower()
    
    if system_== "1":
        add=can_inventory.add_item()
        print(f"Item added: {add[0]}, price: ${add[1]}, quantity: {add[2]}")
        
    elif system_=="2":
        remove=can_inventory.remove_item()
        print(f"Item added: {remove[0]}, price: ${remove[1]}, quantity: {remove[2]}")
        
    elif system_ =="3":
        can_inventory.view_inventory()
        
    elif system_ =="4":
        can_inventory.search_item()
        
    elif system_ =="5":
        can_inventory.calculate_inventory()
        
    elif system_("6"):
        print("Program Terminated!")
        break
