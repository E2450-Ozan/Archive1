year = int(input("Please enter a year to see if it is a leap year: "))  
if (year % 4) == 0:  
   if (year % 100) == 0:  
       if (year % 400) == 0:  
           print("{0} is a leap year.".format(year))  
       else:  
           print("{0} isn't a leap year.".format(year))  
   else:  
       print("{0} is a leap year.".format(year))  
else:  
   print("{0} is not a leap year.".format(year))

