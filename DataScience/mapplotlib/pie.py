import matplotlib.pyplot as plt

slices = [8,12,2,9]
activities = ['skyblue','violet','red','blue']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= Flase,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')

plt.title('pie graph')
plt.show()
