lucky_numbers = [15, 8, 94, 16, 42, 68]
friends = ['jenny', 'kevin', 'june', 'kody', 'buffy', 'angel', 'buffy']
acquaints = ['jim', 'oscar', 'sarah']
friend = ['jenny', 22, False]


print(friends)
print(friends.index('kevin'))
print(friends.count('buffy'))
print(friends[2:5])
friends.extend(acquaints)
friends.append('stewart')
print(friends)
friends.insert(3, 'Johnny')
print(friends)
friends.remove('june')
print(friends)
friends2 = friends.copy()
friends.clear()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)
print(friends2)

""" tuples are immutable and their order is preserved. Values stored inside lists remain their mutability"""

my_tuple = ('a', 'b', [1, 2, 3])
print(my_tuple)
my_tuple[2][0] = 10
print(my_tuple)
my_tuple[2].append(4)
print(my_tuple)
my_tuple[2].clear()
print(my_tuple)