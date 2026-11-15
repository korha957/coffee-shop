from Order import orders

def calculate_total():
    total = 0

    for order in orders:
        total += order["price"] * order["quantity"]

    return total

def calculate_discount(total):
    if total > 1000000:
        discount = total * 0.10
    else:
        discount = 0

    return discount

def print_invoice():
    if len(orders) == 0:
        print("There are no orders to generate an invoice for.")
        return

    print("\n========== Invoice ==========")

    for order in orders:
        print(f"Product: {order['product']}")
        print(f"Quantity: {order['quantity']}")
        print(f"Price: {order['price'] * order['quantity']}")
        print("-----------------------------")

    total = calculate_total()
    discount = calculate_discount(total)
    final_price = total - discount

    print(f"Total: {total}")
    print(f"Discount: {discount:.0f}")
    print(f"Final Price: {final_price:.0f}")

    print("=============================")
