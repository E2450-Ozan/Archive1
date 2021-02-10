#converts the given milliseconds into hours, minutes, and seconds.
number = input("""###  This program converts milliseconds into hours, minutes, and seconds ### \n
(To exit the program, please type "exit")\n
Please enter the milliseconds (should be greater than zero) :  """)
def calculate(num):
    if num < 1000:
        print(f"just {num} millisecons", end=" ")
    else:
        if (num//(1000*60*60)) != 0:
            print(f"{(num//(1000*60*60))} hour/s", end=" ")
        if (num//(1000*60)) != 0 and (num//(1000*60)%60) > 0:
            print(f"{(num//(1000*60))%60} minute/s", end=" ")
        if (num//1000) != 0 and (num//1000)%60 > 0:
            print(f"{(num//1000)%60} seconds/s", end=" ")
    print()
counter = 0
while True:
    if counter != 0:
        number = input()
    if number.lower() == "exit":
        print("Exiting the program ... Good Bye")
        break
    elif number.isdigit() == False:
        print("Not Valid Input !!!")
    elif int(number) <1:
        print("Not Valid Input !!!")
    else:
        number = int(number)
        calculate(number)
    counter += 1