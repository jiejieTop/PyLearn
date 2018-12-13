people = {
    'jiejie' : {
        'phone' : '1234',
        'addr' : 'jiejie home'
    },
    'nan' : {
        'phone' : '3456',
        'addr' : 'nan home'
    }
}

labels = {
    'phone' : 'phone number',
    'addr' : 'address'
}

print(people.get('nan'))

print(people.items())

name = input('name : ')
request = input('phone number (p) or address (a) ?')

if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addres'
else:
    print('err')

if name in people:
    print("{}'s {} is {}.".format(name,labels[key],people[name][key]))
else:
    print('not find the people!')



