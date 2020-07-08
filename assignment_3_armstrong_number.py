num = int(input("Please enter a positive number: "))
sum = 0
temp = num
converted_num = str(num)
n = (len(converted_num))
if num < 0:
    print("You have entered an invalid value.")
elif type(num) != int:
    print("You have entered an invalid value.")
else:
    while temp >0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

