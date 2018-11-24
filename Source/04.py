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

name = input('name : ')
request = input('phone number (p) or address (a) ?')

if request == 'p':
    key = 'phone'
else:
    key = 'addres'

if name in people:
    print("{}'s {} is {}.".format(name,labels[key],people[name][key]))

