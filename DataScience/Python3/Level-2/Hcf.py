#finding the Hcf of the given numbers
_author__ = "Dilipbobby"
#function that finds hcf of given numbers
def hcf(x, y):  
   if x > y:  
       smaller = y  
   else:  
       smaller = x  
   for i in range(1,smaller + 1):  
       if((x % i == 0) and (y % i == 0)):  
           hcf = i  
   return hcf  
  
#Taking input from user
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))
#using the function hcf  
print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  
