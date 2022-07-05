from collections import Counter, OrderedDict


def collections_mod():
    list = ["a", "c", "c", "a", "b", "a", "a", "b", "c"]
    cnt = Counter(list)
    od = OrderedDict(cnt.most_common())
    for key, value in od.items():
        print(key, value)

    """
    List and Tuple objects are sequences. A dictionary is a hash table of key-value pairs. 
    List and tuple is an ordered collection of items. Dictionary is unordered collection.

    List and dictionary objects are mutable i.e. it is possible to add new item or delete 
    and item from it. Tuple is an immutable object. Addition or deletion operations are 
    not possible on tuple object.
    
    Tuples are faster and consume less memory (than lists).

    Each of them is a collection of comma-separated items. List items are enclosed in 
    square brackets [], tuple items in round brackets or parentheses (), and dictionary 
    items in curly brackets {}
    
    A Set is an unordered collection data type that is iterable, mutable, and has no 
    duplicate elements. Python’s set class represents the mathematical notion of a set.
    
    Sets are mutable, and may therefore not be used, for example, as keys in dictionaries.

    Another problem is that sets themselves may only contain immutable (hashable) values, 
    and thus may not contain other sets.

    Because sets of sets often occur in practice, there is the frozenset type, which 
    represents immutable (and, therefore, hashable) sets.
    """

    list1 = [12, "Ravi", "B.Com FY", 78.50]  # list
    tuple1 = (12, "Ravi", "B.Com FY", 78.50)  # tuple
    dictionary1 = {"Rollno": 12, "class": "B.com FY", "precentage": 78.50}  # dictionary
    
    s = set()
 
    # Adding element into set
    s.add(5)
    s.add(10)
    s.add(5)
    print("Adding 5x2 and 10 in set", s)
    
    # Removing element from set
    s.remove(5)
    print("Removing 5 from set", s)
    
    a = set([1, 2, 3, 4])
    b = set([3, 4, 5, 6])
    print(a | b) # Union
    print(a & b) # Intersection
    print(a < b) # Subset
    print(a - b) # Difference
    print(a ^ b) # Symmetric Difference
    c = a.copy()
    print(c)

    a = frozenset([1, 2, 3])
    b = frozenset([2, 3, 4])
    print(a.union(b)) #frozenset([1, 2, 3, 4])
