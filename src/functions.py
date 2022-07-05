import json
from contextlib import suppress


def greetings():
    print("hello world")


def lists():
    colors = ["red", "blue", "green"]
    print(colors[0])  ## red
    print(colors[2])  ## green
    print(len(colors))  ## 3

    squares = [1, 4, 9, 16]
    sum = 0
    for num in squares:
        sum += num
        print(sum)  ## 30

    list = ["larry", "curly", "moe"]
    if "curly" in list:
        print("yay")

    ## print the numbers from 0 through 99
    for i in range(100):
        print(i)

    ## Access every 3rd element in a list
    i = 0
    while i < len(squares):
        print(squares[i])
        i = i + 3

    squares = [1, 4, 9, 16, 25]
    print(squares)

    for i in range(5):
        print(i)
        i += 2

    some_letters = ["a", "b", "c", "d", "e"]
    for letter in some_letters:
        # do something
        pass

    for i, letter in enumerate(some_letters, start=0):
        print(f"item at index {i} is {letter}")

    list = ["larry", "curly", "moe"]
    list.append("shemp")  ## append elem at end
    list.insert(0, "xxx")  ## insert elem at index 0
    list.extend(["yyy", "zzz"])  ## add list of elems at end
    print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
    print(list.index("curly"))  ## 2

    list.remove("curly")  ## search and remove that element
    list.pop(1)  ## removes and returns 'larry'
    print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

    list = [1, 2, 3]
    print(list.append(4))  ## NO, does not work, append() returns None
    ## Correct pattern:
    list.append(4)
    print(list)  ## [1, 2, 3, 4]

    list = ["a", "b", "c", "d"]
    print(list[1:-1])  ## ['b', 'c']
    list[0:2] = "z"  ## replace ['a', 'b'] with ['z']
    print(list)  ## ['z', 'c', 'd']

    print("iter")
    data = {"a": 1, "b": 2, "c": 3}
    for key in data:
        print(key)
    for key in data.keys():
        print(key)
    for value in data.values():
        print(value)
    for key, value in data.items():
        print(key, value)


def json_examples():
    # handling json files
    f = open(
        "test.json",
    )
    data = json.load(f)  # parse JSON from URL or file
    print(data)
    print(data["attribute"])
    print(data["object"])
    print(data["object"]["attribute0"])
    print(data["list"])
    print(data["list"][0]["attribute1"])
    f.close()

    json_str = """{
        "attribute": "value"
    }
    """
    data_loads = json.loads(json_str)  # parse JSON from a string
    print(data_loads)


def files():

    # OLD WAY
    f = open("test.txt")  # note default is mode='r'
    print(f.read())
    f.close()

    # NEW WAY
    with open("test.txt") as f:  # no close() needed
        print(f.read())

    # Echo the contents of a text file
    f = open("test.txt", "rt", encoding="utf-8")
    for line in f:  ## iterates over the lines of the file
        print(line, end="")  ## end='' so print does not add an end-of-line char
        ## since 'line' already includes the end-of-line.
    f.close()

    with open("test.txt", "rt", encoding="utf-8") as f:
        for line in f:
            print(line)  # line is a *unicode* string


def errors():
    # handling errors
    try:
        raise RuntimeWarning("Something could go wrong")
    except RuntimeWarning as e:  # as e is optional
        print(e)


def dicts():
    empty_dict = {}  # or dict()
    my_dict = {"key": "value"}
    # How to get value from dict
    try:
        my_dict["a"]  # raises KeyError if 'a' not in dictionary
    except:
        print("error")

    print(my_dict.get("a", "bob"))

    if "key" in my_dict:
        val = my_dict["key"]
    val = my_dict.get("key", None)
    if val is not None:
        pass
    with suppress(KeyError):
        val = my_dict["key"]
    print(val)

    ## Can build up a dict by starting with the the empty dict {}
    ## and storing key/value pairs into the dict like this:
    ## dict[key] = value-for-that-key
    dict = {}
    dict["a"] = "alpha"
    dict["g"] = "gamma"
    dict["o"] = "omega"

    print(dict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

    print(dict["a"])  ## Simple lookup, returns 'alpha'
    dict["a"] = 6  ## Put new key/value into dict
    print("a" in dict)  ## True
    ## print(dict['z'])                  ## Throws KeyError
    if "z" in dict:
        print(dict["z"])  ## Avoid KeyError

    ## By default, iterating over a dict iterates over its keys.
    ## Note that the keys are in a random order.
    for key in dict:
        print(key)
    ## prints a g o

    ## Exactly the same as above
    for key in dict.keys():
        print(key)

    ## Get the .keys() list:
    print(dict.keys())  ## dict_keys(['a', 'o', 'g'])

    ## Likewise, there's a .values() list of values
    print(dict.values())  ## dict_values(['alpha', 'omega', 'gamma'])

    ## Common case -- loop over the keys in sorted order,
    ## accessing each key/value
    for key in sorted(dict.keys()):
        print(key, dict[key])

    ## .items() is the dict expressed as (key, value) tuples
    print(
        dict.items()
    )  ##  dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])

    ## This loop syntax accesses the whole dict by looping
    ## over the .items() tuple list, accessing one (key, value)
    ## pair on each iteration.
    for k, v in dict.items():
        print(k, ">", v)
    ## a > alpha    o > omega     g > gamma

    h = {}
    h["word"] = "garfield"
    h["count"] = 42
    s = "I want %(count)d copies of %(word)s" % h  # %d for int, %s for string
    print(s)  # 'I want 42 copies of garfield'

    # You can also use str.format().
    s = "I want {count:d} copies of {word}".format(
        **h
    )  # dict needs to be unpacked with the ** operator
    print(s)

    var = 6
    del var  # var no more!

    list = ["a", "b", "c", "d"]
    del list[0]  ## Delete first element
    del list[-2:]  ## Delete last two elements
    print(list)  ## ['b']

    dict = {"a": 1, "b": 2, "c": 3}
    del dict["b"]  ## Delete 'b' entry
    print(dict)  ## {'a':1, 'c':3}
