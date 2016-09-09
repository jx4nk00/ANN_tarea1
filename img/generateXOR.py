from numpy.random import uniform
import numpy as np

x1=uniform(low=-1.0,high=1.0,size=1000)
x2=uniform(low=-1.0,high=1.0,size=1000)

X=np.column_stack((x1,x2))
y=[]
for i in range(0,X.shape[0]):
	if X[i,0]>0 and X[i,1]>0:
		y.append(1)
	else: 
		if X[i,0]<0 and X[i,1]<0:
			y.append(1)
		else:
			y.append(0)	

