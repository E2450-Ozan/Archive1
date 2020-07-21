num = range(1,100)
for i in num :
   print((lambda x: "Fizzbuzz" if x % 3 == 0 and x % 5 == 0 else("fizz" if x % 3 == 0 else ("buzz" if x % 5 == 0 else x)))(i))

