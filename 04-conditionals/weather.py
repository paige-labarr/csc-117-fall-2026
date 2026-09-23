#ask what the temperature is today
#store the user's response as temp
temp = int(input("What is today's temperature? "))


# if temp <= 20:
#     print("Bundle up - it's REALLY cold (hat+gloves)")
# elif temp <= 40:
#     print("Wear a jacket - it's cold")
# else:
#     print("You don't need a jacket - enjoy")

if temp <= 40:
    print("Wear a jacket")
    if temp <= 20:
        print("Also wear a hat and gloves")
else:
    print("You don't need a jacket - enjoy")