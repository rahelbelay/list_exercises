# phonebook_dict = {
#     'Alice': '703-493-2834',
#     'Bob': '857-384-1234',
#     'Elizabeth':'484-584-2923'
# }
# # print elizabeth phone number
# print('1.' )

# print(phonebook_dict['Elizabeth'])

# print('2.' )
# #  add an entry to the existing dictionary

# phonebook_dict['Kareem'] = '938-489-1234'
# print(phonebook_dict)

# print('3.' )
# # delete Alice's phone number
# phonebook_dict.pop('Alice')
# print(phonebook_dict)

# print('4.' )
# #  update Bob's phone no
# phonebook_dict.update({'Bob':'968-345-2345'})
# print(phonebook_dict)

# print('5.' )
# #  print all phone enteries
# print(phonebook_dict)
# list(phonebook_dict)
# print(phonebook_dict)


# Exercise 2 Nested Dictionaries
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies','tennis'],
    'friends':[
        {
        'name':'Jasmine',
        'email':'jasmine@yahoo.com',
        'interests':['photography','tennis']
        },
        {
            'name': 'Jan',
            'email' : 'jan@hotmail.com',
            'interest' : ['movies','tv']
        }
    ]
}
print(Ramit['name']['email'])

