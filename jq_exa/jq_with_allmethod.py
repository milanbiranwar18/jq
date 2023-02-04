import jq

def compile_method_with_all_method():
    obj = jq.compile(".")
    obj1 = obj.input('xyz').all()
    obj2 = obj.input('xyz').first()
    print(obj1)
    print(obj2)

    obj = jq.compile(".[]")
    obj1 = obj.input([1, 2, 3, 4, 'abc', 'bvgh', 5]).all()
    print(obj1)

    obj = jq.compile(".[]+1")
    print(dir(obj))
    obj12345 = obj.input([1, 2, 3, 4, 'abc', 'bvgh', 2.32]).first()
    print(dir(obj12345))
    print(obj12345)



def all_method_with_list_methods():
  
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



if __name__ == '__main__':
    compile_method_with_all_method()
    all_method_with_list_methods()