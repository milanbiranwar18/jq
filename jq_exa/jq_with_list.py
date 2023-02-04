import jq

# print(dir(jq))

def compile_method():

    obj = jq.compile(".")
    obj1 = obj.input('xyz').first()
    print(obj1)

    obj = jq.compile(".")
    obj1 = obj.input(2).first()
    print(obj1)

    obj = jq.compile(".")
    obj1 = obj.input([1, 2, 3, 'abc', 'asd', 2.32, 2.30]).first()
    print(obj1)

    obj = jq.compile(".")
    obj1 = obj.input('xyz').all()
    print(obj1)

    obj = jq.compile(".[]")
    obj1 = obj.input([1, 2, 3, 4, 'abc', 'bvgh', ]).all()
    print(obj1)

    obj = jq.compile(".[]+1")
    obj1 = obj.input([1, 2, 3, 4]).all()
    print(obj1)



def compile_method2():
    obj = jq.compile(".[]")
    obj1 = obj.input([12]).first()
    obj2 = obj.input([12]).all()
    obj3 = obj.input([12]).text()
    print(obj1)
    print(obj2)
    print(obj3)

    obj = jq.compile(".+1")  
    obj1 = obj.input(1).first()
    print(obj1)


    obj = jq.compile(".[]+1")       # this pattern will add 1 in only 0 index position of list 
    obj1 = obj.input([1, 2, 3, 4]).first()
    print(obj1)

    obj = jq.compile("[.[]+1]")       # this pattern will add 1 in each element of input list
    obj1 = obj.input([1, 2, 3, 4]).first()
    print(obj1)

    # obj = jq.compile("[.[]+1]")      # we can't add 1 to string in list it will give error
    # obj1 = obj.input([1, 2, 3, 4, 'abc', 'bvgh', 2.32]).first()       # this statment will give error
    # print(obj1)


    obj = jq.compile(".[]+1.32")       # this pattern will add 1 in only 0 index position of list 
    obj1 = obj.input([1, 2, 3, 4]).first()
    print(obj1)

    obj = jq.compile("[.[]+1.23]")       # this pattern will add 1 in each element of input list
    obj1 = obj.input([1, 2, 3, 4]).first()
    print(obj1)

    # obj = jq.compile("[.[]+1.12]")      # we can't add 1.12 to string in list it will give error
    # obj1 = obj.input([1, 2, 3, 4, 'abc', 'bvgh', 2.32]).first()       # this statment will give error
    # print(obj1)


def compile_method_with_list_methods():
    obj = jq.compile(".")
    obj1 = obj.input("abn").text()
    print(obj1)


    obj = jq.compile(".[]")
    obj1 = obj.input(["abn", 'sdsd', 'sds']).text()
    obj2 = obj.input(["abn", 'sdsd', 'sds', 1, 2, 3]).text()
    print(obj1)
    print(obj2)


    obj = jq.compile(".[]+1")       # this pattern will add 1 in only 0 index position of list 
    obj1 = obj.input([1, 2, 3, 4]).text()
    print(obj1)

    obj = jq.compile("[.[]+1]")       # this pattern will add 1 in each element of input list
    obj1 = obj.input([1, 2, 3, 4]).text()
    print(obj1)



def compile_method_with_list_methods1():
    obj = jq.compile(".[]+1")
    obj1 = obj.input([1, 2, 3, 4]).all()
    print(obj1)

    obj1.append(10)
    print(obj1)

    obj1.clear()
    print(obj1)

    obj1.extend([9, 9, 8, 7, 6, 3, 1])
    print(obj1)

    obj12 = obj1.copy()
    print(obj12, 'copied')

    print(obj1.count(9))

    print(obj1.index(7))

    obj1.pop(0)
    print(obj1)

    obj1.remove(6)
    print(obj1)

    obj1.reverse()
    print(obj1)

    obj1.sort()
    print(obj1)


def compile_method3():
    obj = jq.compile("[.[]*2, -3]")       
    obj1 = obj.input([1, 2, 3, 4]).text()
    print(obj1)

    obj = jq.compile("[.[0], -3]")       
    obj1 = obj.input([1, 2, 3, 4]).text()
    print(obj1)

    obj = jq.compile(".[0]+3, -3")       
    obj1 = obj.input([1, 2, 3, 4]).all()
    print(obj1)

    obj = jq.compile("[.[1]*3, -3]")       
    obj1 = obj.input([1, 2, 3, 4]).text()
    print(type(obj1))
    print(obj1)



if __name__ == '__main__':
    compile_method()
    compile_method2()
    compile_method3()
    compile_method_with_list_methods1()
    compile_method_with_list_methods()