import jq

x = input("input a number")
assert not isinstance(x, int)
print(int(x) + 1)



print(jq.compile(".").input("hello").first() == "hello")
print(jq.compile(".").input("hi").first() == "hello")

print(jq.compile(".").input(text='"hello"').first() == "hello")

print(jq.compile("[.[]+1]").input([1, 2, 3]).first() == [2, 3, 4])
print(jq.compile("[.[]+3]").input([1, 2, 3]).first() == [2, 3, 4])
print(jq.compile("[.[]+3]").input([1, 2, 3]).first() == [4, 5, 6])

print(jq.compile(".[]+1").input([1, 2, 3]).first() == 2)
print(jq.compile(".[]").input([1, 2, 3]).first() == 2)



print(jq.compile(".").input("42").text() == '"42"')

print(jq.compile(".[]").input([1, 2, 3]).text() == "1\n2\n3")

print(jq.compile(".[]+1").input([1, 2, 3]).all() == [2, 3, 4])

iterator = iter(jq.compile(".[]+1").input([1, 2, 3]))
print(next(iterator, None) == 2)
print(next(iterator, None) == 3)
print(next(iterator, None) == 4)
print(next(iterator, None) == None)


program = jq.compile("$a + $b + .", args={"a": 100, "b": 20})
print(program.input(3).first() == 123)


print(jq.first(".[] + 1", [1, 2, 3]) == 2)
print(jq.first(".[] + 1", text="[1, 2, 3]") == 2)
print(jq.text(".[] + 1", [1, 2, 3]) == "2\n3\n4")
print(jq.all(".[] + 1", [1, 2, 3]) == [2, 3, 4])
print(list(jq.iter(".[] + 1", [1, 2, 3])) == [2, 3, 4])

program = jq.compile(".")
print(program.program_string == ".")


obj = jq.compile(".")
print(dir(obj))
obj1 = obj.input('xyz').all()
print(obj1)

print(dir(jq))


