entry = input("Please enter a positive number: ")
lst1 = list(entry)
lst2 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a = True
for i in lst1:
    if i not in lst2:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        a = False
        break
while a:
    num = int(entry)
    if num >= 0:
        num = int(num)
        sum = 0
        temp = num
        converted_num = str(num)
        n = (len(converted_num))
        while temp > 0:
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if num == sum:
            print(num, "is an Armstrong number.")
            break
        else:
            print(num, "is not an Armstrong number.")
            break
    else:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
