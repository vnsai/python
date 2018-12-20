
_author__ = "Dilipbobby"

# Collect input from the user coverting str to flot 
kilometers = float(input('How many kilometers?: '))  
# conversion factor  
#NOTE: kilometer is equal to 0.62137 miles. 2) Kilometer = Miles / 0.62137   
conv_fac = 0.621371  
# calculate miles  
miles = kilometers * conv_fac  
print('%0.3f kilometers is equal to %0.3f miles' %(kilometers,miles))  
#try out miles to kilometers here
