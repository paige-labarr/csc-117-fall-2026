import datetime as dt

# print("Welcome to the Teufort hotel")
# name = input("What is your name? ")
# print(f"Welcome, {name}")
name = "Paige LaBarr"

timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)


vip_file = open("09-files-folders/vip.txt", "r")
vip_list = vip_file.read() #read removes \n from output and goes to next line
print(vip_list)

vip_status = False
for guest_name in vip_list:
    if guest_name.strip() == name:
        vip_status = True
        print("VIP")

file = open("all-guests.txt", "a") #a is for append
file.write(f"{name}, VIP: {vip_status}, Arrival time: {timestamp}\n")
file.close()