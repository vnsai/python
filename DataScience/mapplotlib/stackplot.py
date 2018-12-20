import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleep = [7,8,6,11,7]
eat   =   [2,3,4,3,2]
work  =  [7,8,7,2,2]
play  =  [8,5,7,8,13]


plt.plot([],[],color='c', label='sleep', linewidth=5)
plt.plot([],[],color='m', label='eat', linewidth=5)
plt.plot([],[],color='k', label='work', linewidth=5)
plt.plot([],[],color='r', label='play', linewidth=5)

plt.stackplot(days, sleep,eat,work,play, colors=['c','m','k','r'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('stackplot Graph')
plt.legend()
plt.show()
