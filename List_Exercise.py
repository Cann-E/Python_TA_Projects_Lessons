grocery_list = []


def add_item():
    res1 = input("Enter a grocery item: ")
    grocery_list.append(res1)
    return res1


def remove_item():
    print("Your grocery list:", grocery_list)
    res2 = input("Enter the name of the item you want to remove: ")
    if res2 in grocery_list:
        grocery_list.remove(res2)
        return res2
    else:
        print("Error! Item not in the cart!")
        return None


def view_cart():
    print("Your grocery list:", grocery_list)


while True:
    system_ = input("\nWelcome to the Grocery List Manager!\n"
                    "1-Add Item \n"
                    "2-Remove Item \n"
                    "3-View Cart \n"
                    "4-Exit \n: ").lower()

    if system_ == "1" or system_ == "add item":
        item_add = add_item()
        print(f"'{item_add}' has been added to the cart!")

    elif system_ == "2" or system_ == "remove item":
        removed_item = remove_item()
        if removed_item:
            print(f"'{removed_item}' has been removed from the cart!")

    elif system_ == "3" or system_ == "view cart":
        view_cart()

    elif system_ == "4" or system_ == "exit":
        print("Program Terminated!")
        break

    else:
        print("Invalid option! Please try again.")
