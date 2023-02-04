import jq

def compile_method():
    obj = jq.compile(".")
    obj1 = obj.input('xyz').text()
    print(dir(obj1))
    print(obj1)


    obj = jq.compile(".")
    obj1 = input([1, 2, 3]).text()
    print(type(obj1))
    print(obj1)

if __name__ == '__main__':
    compile_method