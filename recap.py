names = [
    'Daniel',
    'Mike',
    'William'
]

#List comprehension
length = [len(name) for name in names]

print(length)

#DIctionary comprehension
names_length_dict = {name:len(name) for name in names}

print(names_length_dict)