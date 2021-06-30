x = int(input("length :"))
y = int(input("heigth :"))

print(x*"*")
for i in range(1,(y-1)):
    print(f"{(x-(x-i))*' '}*{' '*(x-2)}*")
print(f" {(x-(x-i))*' '}{x*'*'}")


# x = 5
# y = 4

    # print(f" *{' '*(y-2)}*")
    # print(f"  *{' '*(y-2)}*")
    # print(f"   {y*'*'}")

# for i in range(1,x):
#     print(x-(x-i))
