import matplotlib.pyplot as plt

#line 1
x = [1,2,3]
y = [5,8,9]

#line 2
x2 = [1,2,3]
y2 = [15,12,13]

#label is the attribute used to name a line
plt.plot(x, y, label='First Line')
plt.plot(x2, y2, label='Second Line')
#xlabel and ylabel are used to name the axis
plt.xlabel("Plot no's")
plt.ylabel('variance')
#title is used to name the graph 
plt.title('Two line Graph')
#legend is used to show the line_names
plt.legend()

plt.show()
