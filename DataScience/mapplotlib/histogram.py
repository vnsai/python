import matplotlib.pyplot as plt
#ages as list of elements
ages = [15,22,55,62,45,21,22,34,43,42,4,99,102,110,120,121,122,125,111,115,112,80,75,65,54,44,43,42,48]
#in between 
btins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(ages, btins, histtype='bar', rwidth=0.8)

plt.xlabel('ages in btw')
plt.ylabel('age bar')
plt.title('histogram of bar')
plt.legend()
plt.show()
