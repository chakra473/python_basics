x = (input("enter username :\n"))
if len(x) > 3:
    y = "Hello <<UserName>>, How are you?"
    print(y.replace("<<UserName>>", x))
else:
    print("username should contain min 3 char")
