bucket_list = ["visit Italy", "eat pizza in Italy", "eat Cam's pizza in Geneva"]

print(bucket_list[1])
print(len(bucket_list))
bucket_list.append("Go to Las Vegas") #add to end of list
print(bucket_list[3])
print(bucket_list[-1])
bucket_list.insert(0, "Climb Mt Everest") #adds at an index

print("~~~ MY BUCKET LIST ~~~")
for thing in bucket_list:
    print(f"-- {thing}")