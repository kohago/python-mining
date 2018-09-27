# lambda is function without name
def add_paras(int1,int2=1):
    return int1 + int2
print(add_paras(1))
print(add_paras(1,2))


#lambda
def test_lambda():
    add_paras_lambda = lambda int1,int2=1: int1 + int2

    print(add_paras_lambda(1))
    print(add_paras_lambda(1,2))

    #use if in lambda->   a if xxx else b
    get_odd_even = lambda  int1 : "even" if int1 % 2 == 0 else "odd"
    print(get_odd_even(1))
    print(get_odd_even(2))

    #sorted
    #use lambda as sorted(),sort(),min(),max() 's key paramater'
    test_array = ["cat","dog","bird","cow","monkey","fish"]
    print(sorted(test_array))
    print(sorted(test_array,key=len))
    print(sorted(test_array,key = lambda x:x[1]))

    # use lambda as map ,filter 's paramater
    test_int_array =[1,2,3,4,5]
    #Python3からmap()はリストではなくイテレータを返すようになったので注意。
    print(map(lambda x: x*2,test_int_array)) #=> map object! <map object at 0x103e48128>
    print(list(map(lambda x:x*2,test_int_array))) #use list() to convert map to list?

    # use lambda as filter 's paramater
    print(filter(lambda x : x % 2 == 0,test_int_array ))
    print(list(filter(lambda x : x % 2 == 0,test_int_array )))

test_lambda()
