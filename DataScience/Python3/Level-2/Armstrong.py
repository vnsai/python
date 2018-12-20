 
_author__ = "Dilipbobby"
#Note : A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.

#taking i/p from user
number = int(input("Enter a number: "))  
summ = 0  
temp = number  

#while condition 
while temp > 0:  
   digit = temp % 10  
   summ += digit ** 3  
   temp //= 10  
#if condition   
if number == summ:  
   print(number,"is an Armstrong number")  
else:  
   print(number,"is not an Armstrong number")  
