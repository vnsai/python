
_author__ = "Dilipbobby"

"""Note:The Fibonacci sequence specifies a series of numbers where the next number is found by adding up the two numbers just before it."""

#take user i/p
nterms = int(input("How many terms you want? "))  
# first two terms  
frs = 0  
sec = 1  
count = 2  
# check if the number of terms is valid  
if nterms <= 0:  
   print("Plese enter a positive integer")  
elif nterms == 1:  
   print("Fibonacci sequence:")  
   print(frs)  
else:  
   print("Fibonacci sequence:")  
   print(frs,",",sec,end=', ')  
#using while condition
   while count < nterms:  
       nth = frs + sec  
       print(nth,end=' , ')  
       # update values  
       frs = sec  
       sec = nth  
       count += 1  
