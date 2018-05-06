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