# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1coKpqsHinptd7vKuLY2rLxb4xX7-YhTx
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,6])
y=np.array([0,250])

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
x=np.array([0,2,4,6,8,10,12,14,16])
y=np.array([0,50,10,49,1,30,20,45,1])
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np



y=np.array([0,8,1,10,5])


plt.plot(y,marker='o',ms=20,mec='r')
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x1= np.array([0,1,2,3])
y1= np.array([3,8,1,10])
x2= np.array([0,1,2,3])
y2= np.array([6,7,2,11])
plt.plot(x1,y1,x2,y2)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x= np.array([0,1,2,3])
y= np.array([3,8,1,10])

plt.scatter(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x= np.array([0,1,2,3,4,5])
y= np.array([0,2,8,1,14,7])
plt.scatter(x,y,color='red')

x= np.array([12,16,18,26,28,30])
y= np.array([5,6,3,7,17,19])
plt.scatter(x,y,color='blue')

plt.show()

import matplotlib.pyplot as plt
import numpy as np


x= np.array([0,1,2,3,4])
y= np.array([3,8,1,10,5])
mycolor=['red','purple','lime','blue','yellow']

plt.scatter(x,y,color=mycolor)

plt.show()

import matplotlib.pyplot as plt
import numpy as np


x= np.array([0,1,2,3,4])
y= np.array([3,8,1,10,5])
mycolor=['red','purple','lime','blue','yellow']
size=[10,60,120,80,20]

plt.scatter(x,y,color=mycolor,s=size)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['a','b','c','d'])
y=np.array([5,8,10,12])

plt.bar(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array(['a','b','c','d'])
y=np.array([5,8,10,12])

plt.bar(x,y,width=0.1)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=np.array([5,8,10,12])


plt.pie(y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]
plt.pie(y,labels=mylabels)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]

plt.pie(y,labels=mylabels,startangle=90)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]
myexplode=[0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode)

plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]
myexplode=[0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,shadow=True)

plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]
mycolor=['red','purple','lime','blue','yellow']
myexplode=[0.2,0,0,0]
plt.pie(y,labels=mylabels,startangle=90,explode=myexplode,colors=mycolor)

plt.show()

import matplotlib.pyplot as plt
import numpy as np


x=np.array([5,8,10,12])
mylabels=["Apples","Bananas","cherries","dates"]


plt.pie(y,labels=mylabels)
plt.legend()
plt.show()