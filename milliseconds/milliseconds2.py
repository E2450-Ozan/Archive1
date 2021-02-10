print("###  This program converts milliseconds into hours, minutes, and seconds ###")
print("""(To exit the program, please type "exit")""")
### print("Please enter the milliseconds (should be greater than zero) :")
number = 0
def miliseconder(number):
    number = input("Please enter the milliseconds (should be greater than zero) :")
    while number == "exit":
        return("Exiting the program... Good Bye")
        break
    while number != "exit":
        digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
        numset = set(number)
        lennum1 = len(numset - digits)
        if lennum1 > 0:
            print("Not Valid Input !!!")
            return miliseconder(number)
        if int(number) > 0:
            number = int(number)
            numhour = number // 3600000
            nummin = (number - (numhour * 3600000)) // 60000
            numsecond = (number - ((numhour * 3600000) + (nummin * 60000))) // 1000
            if numhour == 0 and numsecond == 0 and nummin == 0:
                print(number, "milisecond/s")
            elif nummin == 0 and numsecond== 0:
                print(numhour, "hour/s")
            elif numhour == 0 and numsecond == 0:
                print(nummin, "minute/s")
            elif numhour == 0 and nummin == 0:
                print(numsecond, "second/s")
            elif numhour == 0:
                print(nummin, "minute/s", numsecond, "second/s")
            elif numsecond == 0:
                print(numhour, "hour/s", numsecond, "minute/s")
            elif nummin == 0:
                print(numhour, "hour/s", numsecond, "second/s")
            else:
                print(numhour, "hour/s", nummin, "minute/s", numsecond, "second/s")
            return miliseconder(number)
        else:
            print("Not Valid Input !!!")
            return miliseconder(number)
print(miliseconder(number))