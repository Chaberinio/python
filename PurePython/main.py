'''my_dict = {}
my_dict['drzewo'] = 'liściaste'
print(my_dict)
my_dict['drzewo'] = 'iglaste'
print(my_dict)
del my_dict['drzewo']
print(my_dict)
print(my_dict.get('drzewo', 'nie ma'))'''

'''colors = ['red', 'green', 'red', 'blue', 'green', 'red', 'orange', 'purple', 'red']
counted_colors = {}

for x in colors:
    if x in counted_colors:
        counted_colors[x] += 1
    else:
        counted_colors[x] = 1

print(counted_colors)

print(set(colors))'''

names = ['Ala', 'Ela', 'Ola', 'Iwona', 'Ilona', 'Adam', 'Robert', 'Małgorzata', 'Dagmara']

'''genders = {'Male': [], 'Female': []}

for x in names:
    if x.endswith('a'):
        genders['Female'] += [x]
    else:
        genders['Male'] += [x]


print(genders['Male'])
print(genders['Female'])'''

name_length = {}

for x in names:
    if len(x) in name_length:
        name_length[len(x)] += [x]
    else:
        name_length[len(x)] = [x]

print(name_length)