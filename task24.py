email = input("email: ")

if email.startswith("@") and email.endswith(".com"):
    print(True)

else:
    print(False)