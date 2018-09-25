a = 100;


def testfunc():
    a = 300; # local variable stays in function scope
    return a + 30;


print(testfunc());


def testfunc2(name, age, likes='JavaScript'):
    string = 'User name is {}, age {}, likes {}';
    print(string.format(name, age, likes));


testfunc2('Parthib', 30, 'python')
testfunc2('Parthib', 30)
