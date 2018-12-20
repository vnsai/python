
_author__ = "Dilipbobby"

#take user input 
num = int(input("Enter a number: "))  
#condition to check a number as pos or negative 
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0  
# use while loop to iterate un till zero  
   while(num > 0):  
       sum += num  
       num -= 1  
   print("sum all natural no's is",sum)  
