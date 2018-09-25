# packing is similar to JS rest operator in function
# it creates a tuples of given list or strings


numbers = [1, 2, 3, 4]
print(numbers)


# usage when unknown number of arguments are possible in a function

def test_func(*params):  # *args
    for param in params:
        print(param)


test_func(1, 4, 6, 7, 8)

# dictionary ** usage in keywords


def test_func2(name, age, likes, ):
    string = 'Meet {}, age {}, likes {}'.format(name, age, likes)
    print(string)


dict_def = {
    'name': 'Parthib',
    'age': '28',
    'likes': 'Python'
}

test_func2(**dict_def)  # **kwargsRR

# another usage


def test_func3(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


test_func3(name='parthib', age='28')
