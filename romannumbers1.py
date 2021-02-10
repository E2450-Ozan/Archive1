
#converts the given number to the Roman
number = input("Please enter a number between 1 and 3999, inclusively: \n")
while True:
    if number.isdigit()==False:
        print(f"Not Valid Input !!!")
        number = input("Please enter a number between 1 and 3999, inclusively: \n")
    else:
        numberlocal = int(number)
        if numberlocal < 1 or numberlocal > 3999:
            print(f"Not Valid Input !!!")
            number = input("Please enter a number between 1 and 3999, inclusively: \n")
        else:
            break
list=[]
while True:
    if number[-1] == "4":
        list.append("IV")
    elif number[-1] == "9":
        list.append("IX")
    else:
        list.append((((int(number[-1])//5)*"V")+(int(number[-1])%5)*"I"))
    if len(number) > 1:
        if number[-2] == "4":
            list.append("IL")
        elif number[-2] == "9":
            list.append("IC")
        else:
            list.append((((int(number[-2])//5)*"L")+(int(number[-2])%5)*"X"))
    if len(number) > 2:
        if number[-3] == "4":
            list.append("ID")
        elif number[-3] == "9":
            list.append("IM")
        else:
            list.append((((int(number[-3])//5)*"D")+(int(number[-3])%5)*"C"))
    if len(number) > 3:
        list.append(int(number[-4])*"M")
    break
print("".join(list[::-1]))