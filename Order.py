from Menu import menu

orders = []

def add_order():
    product = input("Enter product name: ").lower()

    if product not in menu:
        print("This product is not available on the coffee shop menu!")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            return

        order = {
            "product": product,
            "price": menu[product],
            "quantity": quantity
        }

        orders.append(order)

        print("Order added successfully.")

    except ValueError:
        print("Please enter the quantity as a number!")

def show_orders():
    if len(orders) == 0:
        print("No orders have been placed yet.")
        return

    print("\n========== Orders ==========")

    for order in orders:
        print(f"Product: {order['product']}")
        print(f"Price: {order['price']}")
        print(f"Quantity: {order['quantity']}")
        print("----------------------------")