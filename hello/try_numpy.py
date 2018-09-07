'''
Created on 2018/03/28

@author: syuu
'''
import numpy;

def test_basic():
    na=numpy.array([[1,2,3],[4,5,6]])
    nb=numpy.array([[-1,-2,-3],[1,1,1]])
    print(na+nb)
    print(na*nb)
    
    nc=numpy.array([[2,4],[3,6],[4,8]])
    print(na.dot(nc))
    
test_basic()