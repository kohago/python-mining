'''
Created on 2018/04/08

@author: syuu
'''
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
from matplotlib import pyplot

x=np.array([[1,2],[2,1],[3,4],[4,3]])
z=linkage(x,'ward')
dendrogram(z)
pyplot.show()