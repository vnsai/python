
#addition of two matrix elements
_author__ = "Dilipbobby"

#3x2 matrix
A = [[1,2,3],  
       [4,5,6],  
       [7,8,9]]  
  
B = [[10,11,12],  
       [13,14,15],  
       [16,17,18]]  
  
Result = [[0,0,0],  
                [0,0,0],  
                [0,0,0]]  
# iterate through rows  
for i in range(len(X)):  
   # iterate through columns  
   for j in range(len(A[0])):
#aadition of elements  
       result[i][j] = A[i][j] + B[i][j]  
for r in result:  
   print(r)  
