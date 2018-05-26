l = lambda x, y : x / y
print(l(5, 2))

#lists
my_list_1 = list(range(10))
my_list_2 = [10,11,12]
print(1 in my_list_1 and 1 in my_list_2)

#tuples
my_tuple = (1, 2)

try:
    my_tuple[0] = 3
except TypeError:
    print('Unable to change tuple')

#dictionaries
my_dict = {'Joel' : 80, 'Tim' : 95 }
print(my_dict['Joel'])

try:
    print(my_dict['Kate'])
except:
    print("Unable to read empty key")

print('Kate' in my_dict)
print(my_dict.get('Kate', 0))

#defaultdict
from collections import defaultdict
import docx2txt

document = docx2txt.process(r"C:\Диссертация\статьи-20170718T143901Z-001\статьи\2017\Журнал Автоматизация\подрисуночные подписи.docx")
word_counts = defaultdict(int)
for word in document.split(' '):
    word_counts[word] += 1

print(word_counts)

#Counter
from collections import Counter
c = Counter(document.split(' '))
print(c)

#sets
s = set()
s.add(1)
s.add(2)
s.add(2)
print(s)

s2 = set([1,1,1,2,2,2,3,3,3])
print(s2)

#if else
def parity(x):
    return "четное" if x % 2 == 0 else "нечетное"

print(parity(5))
print(parity(4))

#sort
print('-------sort--------')
x = [4,1,2,3]
print(x)
y = sorted(x)
print(x)
print(y)
x.sort()
print(x)

x = sorted([-4, 1, -2, 3], key=abs, reverse=True)
print(x)

#sequence generators
print('-------sequence generators--------')
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)

square_dict = {x : x * x for x in range(5)}
print(square_dict)
square_set = { x * x for x in [-1, 1]}
print(square_set)

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]
print(increasing_pairs)

#generator functions
print('-------generator functions--------')

def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

lazy_evens_below_20 = (i for i in lazy_range(20) if i % 2 == 0)
print([x for x in lazy_evens_below_20])

#random
print('-------random--------')

import random

four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)

print(random.randrange(3, 6))

up_to_ten = [x for x in range(10)]
random.shuffle(up_to_ten)
print(up_to_ten)

my_best_friend = random.choice(["Alice", "Bob", "Joe"])
print(my_best_friend)

winning_numbers = random.sample(range(60), 6)
print(winning_numbers)

#oop
print('-------oop--------')

class Set:

    def __init__(self, values=None):
        self.dict = {}

        if values is not None:
            for value in values: self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1,2,3])
s.add(4)
print(s.contains(4))
s.remove(3)
print(s.contains(3))


#zip
list1 = ['a', 'b', 'c']
list2 = [1,2,3]
print(list(zip(list1, list2)))

pairs = [('a', 1), ('b', 2), ('c', 3)]
print(list(zip(*pairs)))


#args and kwargs
def doubler(f):
    def g(x):
        return 2 * f(x)
    return g

def f1(x):
    return x + 1

g = doubler(f1)

def f2(x, y):
    return x + y

#g = doubler(f2)
#print(g(1, 2))

print(g(3))

def magic(*args, **kwargs):
    print('unnamed: ', args)
    print('key args: ', kwargs)

magic(1, 2, 3, key="word", key2='word2')


def other_magic(x, y, z):
    return x * y * z

x_y_list = [1, 2]
z_dict = {'z' : 3}
print(other_magic(*x_y_list, **z_dict))


def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

g = doubler_correct(f2)
print(g(1,2))
