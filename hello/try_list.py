
test_str_array = ["cat","dog","bird","cow","monkey","fish"]
test_int_array =[1,2,3,4,5]

#comprehension
def test_comprehension():
    #list comprehension 内包表示
    comprehension_str_array = [ x * 3 for x in test_str_array ]
    print(comprehension_array) # ['catcatcat', 'dogdogdog', 'birdbirdbird', 'cowcowcow', 'monkeymonkeymonkey', 'fishfishfish']

    comprehension_int_array = [ x * 3 for x in  test_int_array]
    print(comprehension_int_array)

#test_comprehension()

#generic
def test_generic():
    g_ary = (x **2 for x in test_int_array)
    print(g_ary)
    print(list(g_ary))

#test_generic()
