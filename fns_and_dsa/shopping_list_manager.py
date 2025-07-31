# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✅ Inside main

    while True:
        display_menu()  # ✅ Called each loop

        choice = input("Enter your choice: ")  # ✅ Input is a string

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")  # ✅ f-string
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")  # ✅ f-string
            else:
                print(f"'{item}' not found in the shopping list.")  # ✅ f-string
        elif choice == '3':
            if shopping_list:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")  # ✅ f-string
            else:
                print("Your shopping list is currently empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
