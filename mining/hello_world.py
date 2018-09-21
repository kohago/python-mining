
'''
Created on 2018/03/25

@author: syuu
'''

import math

def test_array(arr=None):
    if arr is None:
      arr= ['Tokyo', 'Osaka', 'Fukuoka']
    for u in arr:
        print(u)
    s = []
    for u in range(5):
        s.append(u * 2)
    print(s)
    print(s[2:5])

    input = [1, 3, 5, 7, 9]
    outputArr = [u * 2 for u in input if u > 3]
    print(outputArr)

def test_math(x=1/2):
    print(math.floor(x))
    print(math.ceil(x))
    print(3**3)

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

def test_if():
    for x in range(10):
        if x>2:
            print(x," is bigger than 2")
        elif x>4:
            print(x,' is bigger than 4')
        else:
            print(x ,'is others')
    for y in range(11,20):
        if y % 2 ==0:
            continue
        if y > 15:
            break
        print(y)

def test_function_para(first,*second,**third):
    print("the first parameter is ",first)
    for sec in second:
        print("one of the second paramter is ",sec)
    for thr in third:
        print("one of the third paratmer is ",thr,":",third[thr])

print("Hello World")
test_array()
test_math()
test_dictionary()
test_enumerateAndZip()
test_if()
test_function_para("human","dog","bird","cat",
                   one="one",two="two")
