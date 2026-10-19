groceries = ["milk", "apples", "eggs", "butter", "raspberries"]

groceries.append("apples")
groceries.append("bread")
groceries.append("cantaloupe")

item = groceries.pop(groceries.index("apples"))
groceries.clear()

print(groceries)

scores = [70000, 75000, 62455, 80120, 68754]
scores.sort(reverse=True)
print(scores)