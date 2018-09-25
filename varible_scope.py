a = 100;

def testFunc():
    a = 300; # local variable stays in function scope
    return a + 30;
def testFunc2():
    global a; # allow to chnage in global scope
    a = 300;
    return a +10;

print(testFunc());
print(a)
print(testFunc2());
print(a)


# list and object can be updated with out using global keyword

list = [10, 'test', 12.5]

def testFunc3():
    list[0] = 11;
    list[1] = 'updatedTest'
    return list;
print(testFunc3())
