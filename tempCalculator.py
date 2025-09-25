choice = int(
    input("Enter 1 for cel to feh coversion \nEnter 2 for feh to cel conversion \n :")
)

if choice == 1:
    cel = float(input("enter cel : "))
    print("the conversion of cel into feh is : ", (cel * 9 / 5) + 32)

elif choice == 2:
    fer = float(input("enter fer : "))
    print("the conversion of fer into cel is : ", ((fer - 32) * 5) / 9)

else:
    print("enter from choise ")


# cel = int(input("Enter temp in celsius : "))
# fer = (cel * 9/5) + 32
# print("cel in feh is ", fer)
