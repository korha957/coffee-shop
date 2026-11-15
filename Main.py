from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, print_invoice

def main():

    while True:

        print("\n========== Coffee Shop ==========")
        print("1. Show Coffee Menu")
        print("2. Add Order")
        print("3. Show Orders")
        print("4. Calculate Total Amount")
        print("5. Print Invoice")
        print("6. Exit")
        print("=================================")

        choice = input("Your choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            add_order()

        elif choice == "3":
            show_orders()

        elif choice == "4":
            total = calculate_total()
            print(f"Total order amount: {total}")
        elif choice == "5":
            print_invoice()

        elif choice == "6":
            print("Thank you for your purchase!")            
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()