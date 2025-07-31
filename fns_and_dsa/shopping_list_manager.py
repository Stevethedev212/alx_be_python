# shopping_list_manager.py

shopping_list = []  

def display_menu():  
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")  
    else:
        print("Item name cannot be empty.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")  
    else:
        print(f"'{item}' is not in the shopping list.")  

def view_list():
    if shopping_list:
        print("\nCurrent Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")  
    else:
        print("\nYour shopping list is currently empty.")

def main():
    while True:
        display_menu() 

        try:
            choice = int(input("Choose an option (1-4): ").strip())  
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            add_item()
        elif choice == 2:
            remove_item()
        elif choice == 3:
            view_list()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
