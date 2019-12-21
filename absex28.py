Mypets = ['Zophie', 'Pooka', 'Fat-tail']
name = input('Enter a pet name:')
if name not in Mypets:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet.')
