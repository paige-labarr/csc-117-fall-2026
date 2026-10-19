total = 0
counter = 1
while counter <= 6:
    if counter % 2 == 0:
        total += counter * 2
    else:
        if counter == 3:
            total += 10
        else:
            total += 1

    counter += 1

print(total)
