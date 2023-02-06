import jq

def compile_method_with_dictionary_input():
    obj = jq.compile(".")
    obj1 = obj.input({"hi":42, "abc":"abcde"}).all()
    print(obj1)

    obj = jq.compile(".abc")
    obj1 = obj.input({"hi":42, "abc":"abcde"}).all()
    print(obj1)

    obj = jq.compile("{(.abc): .hi}")
    obj1 = obj.input({"hi":42, "abc":"abcde"}).all()
    print(obj1)

    obj = jq.compile("{(.hi): .abc}")
    obj1 = obj.input({"hi":'42', "abc":"abcde"}).first()
    print(obj1)


def jq_with_dictionary_methods():
    obj = jq.compile(".")
    obj1 = obj.input({"hi":'42', "abc":"abcde"}).first()
    print(obj1)

    obj2 = obj1.get('hi')
    print(obj2)

    obj3 = obj1.items()
    print(obj3)

    obj4 = obj1.keys()
    print(obj4)

    obj5 = obj1.values()
    print(obj5)

    obj1.update({'hi':'123', 'name':'raj'})
    print(obj1)

    obj1.pop('hi')
    print(obj1)

    obj1.popitem()
    print(obj1)


def jq_module_with_dictionary():

        
    obj = jq.compile(".")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}]).first()
    print(obj1)

    obj = jq.compile(".[]")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}]).first()
    print(obj1)

    obj = jq.compile(".[0]")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}]).first()
    print(obj1)

    obj = jq.compile(".[1]")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}]).first()
    print(obj1)

    obj = jq.compile(".[2]")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}, {"name":"raj", "city":"pune"}]).first()
    print(obj1)

    obj = jq.compile(".[2].name")
    obj1 = obj.input([{"hi":42, "abc":"abcde"}, {"name":"milan", "city":"pune"}, {"name":"raj", "city":"pune"}]).first()
    print(obj1)




if __name__ == '__main__':
    # compile_method_with_dictionary_input()
    # jq_with_dictionary_methods()
    jq_module_with_dictionary()