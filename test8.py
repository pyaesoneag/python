# height = float(input("Enter height : "))
# if height >= 5.6:
#     print("You are tall")
# else:
#     print("You are short")

answer = input("""
 Type 1 for 100MB,
 Type 2 for 200MB,
 Type 3 for 300MB,
 """)
if answer == "1":
    print("100 MB Purchased ")
elif answer == "2":
    print("200 MB Purchased ")
elif answer == "3":
    print("300 MB Purchased ")
else:
    print("Type 1 , 2 , 3 only")
