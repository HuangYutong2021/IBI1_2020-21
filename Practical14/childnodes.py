from xml.dom.minidom import parse
import xml.dom.minidom
import re
import matplotlib.pyplot as plt
all = {}
mark=[]

def searchall(na):
  if na != []:
    for x in na:
        if x not in mark:
            mark.append(x)
        searchall(all[x])
dom = xml.dom.minidom.parse('go_obo.xml')
collection = dom.documentElement
collections = collection.getElementsByTagName("term")
for i in collections:
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    all[Name]=[]
for i in collections:
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    s = i.getElementsByTagName("is_a")
    if s.length > 0:
        for q in s:
         name = q.childNodes[0].data
         all[name].append(Name)
for i in collections:
    data = i.getElementsByTagName("defstr")[0].childNodes[0].data
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    if re.search('DNA',data):
       searchall(all[Name])
mark1=len(mark)
print('DNA:',mark1)
mark=[]
for i in collections:
    data = i.getElementsByTagName("defstr")[0].childNodes[0].data
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    if re.search('RNA',data):
       searchall(all[Name])
mark2=len(mark)
print('RNA:',mark2)
mark=[]
for i in collections:
    Data = i.getElementsByTagName("defstr")[0].childNodes[0].data
    data= Data.lower()
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    if re.search('protein',data):
       searchall(all[Name])
mark3=len(mark)
print('Protein:',mark3)
mark=[]
for i in collections:
    Data = i.getElementsByTagName("defstr")[0].childNodes[0].data
    data = Data.lower()
    Name = i.getElementsByTagName("id")[0].childNodes[0].data
    if re.search('carbohydrate',data):
       searchall(all[Name])
mark4=len(mark)
print('Carbohydrate:',mark4)

labels = 'DNA','RNA','Protein','Carbohydrate'
sizes = [mark1,mark2,mark3,mark4]
explode = (0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
plt.axis('equal')
plt.title("which is the most complex? Protein!")
plt.show()