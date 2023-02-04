import jq

# print(dir(jq))

def jq_first_method():

    obj1 = [1, 2, 3]
    obj = jq.first(".", obj1)
    print(obj)

    obj1 = [1, 2, 3]
    obj = jq.first(".[]+1", obj1)
    print(obj)

    obj1 = [1, 2, 3]
    obj = jq.first("[.[]+1]", obj1)
    print(obj)

    obj1 = [1, 2, 3]
    obj = jq.first("[.[]*2, -3]", obj1)
    print(obj)




def jq_text_method():

    obj = [1, 2, 3]
    obj1 = jq.text(".", obj)
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.text(".[]+1", obj)
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.text("[.[0]+1, -4]", obj)
    print(obj1)

    obj = "cef"
    obj1 = jq.text(".", obj)
    print(obj1)



def jq_all_method():

    obj = "cef"
    obj1 = jq.all(".", obj)
    print(dir(obj1))
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.all(".", obj)
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.all(".[]+1", obj)
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.all(".[0]-1, -4", obj)
    print(obj1)

    obj = [1, 2, 3]
    obj1 = jq.all("[.[0]+1, -4]", obj)
    print(obj1)

    obj1 = [1, 2, 3]
    obj = jq.all(".[]*2, -3", obj1)
    print(obj)


def jq_iter_method():

    obj = [1, 2, 3]
    obj1 = jq.iter(".", obj)
    print(next(obj1))

    obj1 = [1, 2, 3]
    obj = jq.iter(".", obj1)
    print(next(obj))

    obj1 = [1, 2, 3]
    obj = jq.iter(".[]+1", obj1)
    print(next(obj))

    obj1 = [1, 2, 3]
    obj = jq.iter("[.[]+1]", obj1)
    print(next(obj))

    obj1 = [1, 2, 3]
    obj = jq.iter("[.[]*2, -3]", obj1)
    print(next(obj))



if __name__ == '__main__':
    jq_all_method()
    jq_first_method()
    jq_iter_method()
    jq_text_method()
