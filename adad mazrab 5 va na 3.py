list = [i for i in range(20,201)]
for i in reversed(list):
    if i % 5 != 0 or i % 3 == 0:
        continue
    else:
        print(i, end=" ")
        