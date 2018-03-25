'''
Created on 2018/03/25

@author: syuu
'''

import math
from builtins import input

if __name__ == '__main__':
    
    def test_array():
        for u in ['Tokyo', 'Osaka', 'Fukuoka']:
            print(u)
        s = []
        for u in range(5):
            s.append(u * 2)
        print(s)
        print(s[2:5])
        
        input = [1, 3, 5, 7, 9]
        outputArr = [u * 2 for u in input if u > 3]
        print(outputArr)
        
    def test_math():
        x = 1 / 2
        print(math.floor(x))
        print(math.ceil(x))
    
   
    def test_dictionary():
        dic = {'mouse':1, 'cow':2, 'pig':3, 'tiger':4}
        print(dic['cow'])
        print(dic.items())
        print(dic.keys())
        print(dic.values())
        outputDic = {u:v + 100 for u, v in dic.items()}
        print(outputDic.items())
        print(sorted(dic.items(),key=lambda u:u[1],reverse=True))
    
    def test_enumerateAndZip():
        input= ['Tokyo', 'Osaka', 'Fukuoka']
        for i,v in enumerate(input):
            print(i,v)
        num=[10,20,30]
        for u in zip(input,num):
            print(u)
    
    print("Hello World")
    test_array()
    test_math()
    test_dictionary()
    test_enumerateAndZip()
    
    
