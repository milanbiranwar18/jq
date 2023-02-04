import jq

assert jq.compile(".").input("hello").first() == "hello"

assert jq.compile(".").input("42").text() == '"42"'

assert jq.compile(".[]").input([1, 2, 3]).text() == "1\n2\n3"

assert jq.compile(".[]+1").input([1, 2, 3]).all() == [2, 3, 4]



assert jq.compile(".").input(text='"hello"').first() == "hello"
assert jq.compile("[.[]+1]").input([1, 2, 3]).first() == [2, 3, 4]
assert jq.compile(".[]+1").input([1, 2, 3]).first() == 2


iterator = iter(jq.compile(".[]+1").input([1, 2, 3]))
assert next(iterator, None) == 2
assert next(iterator, None) == 3
assert next(iterator, None) == 4
assert next(iterator, None) == None


program = jq.compile("$a + $b + .", args={"a": 100, "b": 20})
assert program.input(3).first() == 123


assert jq.first(".[] + 1", [1, 2, 3]) == 2
assert jq.first(".[] + 1", text="[1, 2, 3]") == 2
assert jq.text(".[] + 1", [1, 2, 3]) == "2\n3\n4"
assert jq.all(".[] + 1", [1, 2, 3]) == [2, 3, 4]
assert list(jq.iter(".[] + 1", [1, 2, 3])) == [2, 3, 4]


program = jq.compile(".")
assert program.program_string == "."

