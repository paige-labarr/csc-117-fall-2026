# Paige LaBarr
# October 28, 2026
# Midterm Review
# Practice adding names to a list until we're done

import random

# 1 - create a variable called name (string)
# 2 - make an empty list called vip_list
# 3 - make a while loop, condition is name != DONE
# 4 - in loop - prompt user for input to update the name
# 5 - in loop - check if name is DONE
# 6 - in loop - add name to vip_list
# 7 - print the vip_list

name = ""
vip_list = []
while name != "DONE":
    name = input("Add a name to the list: ")
    vip_list.append(name)
vip_list.pop()
print(f"Here's your list: {vip_list}")
        
