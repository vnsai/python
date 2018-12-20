
_author__ = "Dilipbobby"

var = input("Enter a string: ")  
# breakdown the string into a list of words  
words = var.split()  
# sort the list  
words.sort()  
# display the sorted words  
for word in words:  
   print(word)  
