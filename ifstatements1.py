name = input("Please enter your name: ").title().strip()
if 'Matt' == name:
        print("Hello, {yourname}! The password is : W@12".format(yourname = name))
elif 'Matt Alton' == name:
        print("Hello, {yourname}! The password is : W@12".format(yourname = name))
else: 
    print("Hello, {yourname}! See you later.".format(yourname = name))

