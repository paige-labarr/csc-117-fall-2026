temp = int(input("What is today's temperature? "))
rain = input("Is it raining? (y/n): ")

if (rain == "yes" or rain == "y") and temp <= 31:
    print("no golf today")
elif rain == "yes":
    print("go check with coach")
else:
    print("it's likely you'll have golf")    