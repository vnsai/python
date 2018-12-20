import matplotlib.pyplot as plt

#reading the list of values as x1,y1
plt.bar([1,3,5,7,13],[5,2,7,8,6], label="BarEg one")
#reading the list of values as x2,y2
plt.bar([2,4,12,8,10],[8,6,3,5,7], label="BarEg two", color='g')
plt.legend()
#naming the x,y axis
plt.xlabel('number')
plt.ylabel('height of bar')
#naming the graph
plt.title("Bar Graph's")
#showing the plot 
plt.show()
