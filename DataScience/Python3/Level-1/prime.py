#find a given number is prime or not
_author__ = "Dilipbobby"

#note :A prime number is a natural number greater than 1 and having no positive divisor other than 1 and itself.


#reading i/p from user
number = int(input("Enter a number: "))  

#checking condition  
if number > 1:  
   for i in range(2,num):  
       if (number % i) == 0:  
           print(number,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(number,"is a prime number")  
         
else:  
   print(number,"is not a prime number")  
