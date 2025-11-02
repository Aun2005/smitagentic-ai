products = {"apple":1.50, "banana":0.75, "orange":1.2}
productName = input("Enter product name (apple, banana, orange): ").lower()
if productName in products:
    print(f"The price of {productName} is ${products[productName]:.2f}")