comment = input("Izohni kiriting: ")

clean_comment = comment.lower()

if "bad" in clean_comment:
    print(True)
else:
    print(False)
