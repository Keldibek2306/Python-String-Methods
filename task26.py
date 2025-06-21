username = input()

cleaned = username.replace("-", "")

if cleaned.isalnum():
    print(True)
else:
    print(False)
