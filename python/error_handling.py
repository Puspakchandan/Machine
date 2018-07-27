# Basic adding two number when error occurs
  
try:
   number1 = int(input("please Enter the number"))
   number2 = int(input("please Enter the another value"))
  

   result = number1 / number2
   print (result) 

except ZeroDivisionError as e:
   print ("there is an error occurs")
   print ("Entering string Chracter on  integer specific")
    

# Type Error Exception 
try:
   x = 50
   y = "Three"

   z = x + y
   print (z) 

except TypeError as e:
   print ("The Value intiger is not added with straing Character")





     

      
