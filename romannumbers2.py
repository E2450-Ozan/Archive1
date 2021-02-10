nums = [1,4,5,9,10,40,50,90,100,400,500,900,1000,4000]
romans = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
print("###  This program converts decimal numbers to Roman Numerals ###", "\n")
print("(To exit the program, please type 'exit')", "\n")
a= 0
i = nums[0]
num = input("Please enter a number between 1 and 3999, inclusively :").strip().lower()
t = True
while t:
    if num.isdigit() and num != exit and int(num) > 0 and int(num) < 4000:
        k = int(num)
        while i in nums and k > 0:
            if k >= i and k < nums[a+1]:
                print (romans[a], end ="")
                k -= i
                a=0
                i = nums[0]
            else:
                a +=1
                i = nums[a]
        num = input("\nPlease enter a number between 1 and 3999, inclusively :").strip().lower()
    elif num == "exit":
        print("thank you")
        t = False
    else:
        print("enter a valid number!!")
        num = input("Please enter a number between 1 and 3999, inclusively :").strip().lower()
        