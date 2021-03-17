import matplotlib.pyplot as plt
# import matplotlib.pylot and simplify it as plt so that I can use plt to make the pie.
labels = 'USA', 'India', 'Brazil', 'Russia', 'UK'
# record the name of countries in the directory.
sizes = [29862124,11285561,11205972,4360823,4234924]
# record the sizes in the directory
explode = (0,0,0,0,0)
# specify the fraction of the radius to make everyone close to each other.
plt.pie(sizes,explode= explode, labels=labels, autopct='%1.1f%%', shadow= True, startangle=90)
# determine some specific information of the pie.
plt.axis('equal')
# equal aspect ratio ensures the pie is drawn as a circle.
plt.show()
# show the graph
