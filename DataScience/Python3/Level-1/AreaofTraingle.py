
_author__ = "Dilipbobby"

# Three sides of the triangle is a, b and c from input user:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
asp = (a + b + c) / 2  
  
# calculate the area  
area = (asp*(asp-a)*(asp-b)*(asp-c)) ** 0.5  
print('Area of the triangle is %0.2f' %area)   
