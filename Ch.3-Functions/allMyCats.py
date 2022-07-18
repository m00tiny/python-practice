#!/usr/bin/env python3
cat_names = []
while True:
    print('Enter the name of a cat: ' + str(len(cat_names) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    cat_names = cat_names + [name] # list con/cat/enation *hyuk*
print('The cats names are: ')
for name in cat_names:
    print(name + ', ', end='')

