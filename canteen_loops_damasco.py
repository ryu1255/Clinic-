# Activity #7 - Hands-on Activity: "School Canteen Order Tracker"

MENU = {
    "rice meal": 60.0,
    "sandwich": 45.0,
    "juice": 25.0,
    "snack": 30.0
}

orders = {
    "rice meal": 0,
    "sandwich": 0,
    "juice": 0,
    "snack": 0
}

while True:
    item = input("Enter item (rice meal/sandwich/juice/snack or done): ").strip().lower()

    if item == "done":
        break

    if item not in MENU:
        print("Invalid item. Try again.\n")
        continue

    while True:
        qty_text = input("Enter quantity (positive whole number): ").strip()

        if qty_text.isdigit() and int(qty_text) > 0:
            qty = int(qty_text)
            break
        else:
            print("Invalid quantity. Enter 1, 2, 3, ...")
            continue
    
    orders[item] += qty
    print(f"Saved: {item} x{qty}\n")

print("\n=== CANTEEN ORDER SUMMARY ===")
grand_total = 0.0

for food in MENU:
    qty = orders[food]
    price = MENU[food]
    subtotal = qty * price
    grand_total += subtotal
    print(f"{food}: {qty} pcs x {price:.2f} = {subtotal:.2f}")

print(f"GRAND TOTAL: {grand_total:.2f}")
print("=== END ===")


