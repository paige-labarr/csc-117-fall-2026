size = input("small, medium, or large? ")
topping = input("cheese or pepperoni? ")

total = 0

print(f"Ok, one {size} pizza.")
if size == "small":
    total += 8
elif size == "medium":
    total += 15
elif size == "large":
    total += 19.75
else:
    print("We don't have that size.")

if topping == "pepperoni":
    if size == "small":
        total += 1
    elif size == "medium":
        total += 1.25
    elif size == "large":
        total += 2.50

print(f"Ok that's a {size} {topping} pizza.")
print(f"Your total is ${total}.")