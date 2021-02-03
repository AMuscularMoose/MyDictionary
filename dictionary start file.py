phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
'''
print()
print('*****  start section 1 - print dictionary ********')
print()


#print(phonebook)



print()
print('*****  end section 1 ********')
print()






print()
print('*****  start section 2 - search dictionary ********')
print()


if 'Chris' in phonebook:
    print(phonebook['Chris'])
else:
    print('Chris is not in the phonebook')



print()
print('*****  end section 2 ********')
print()






print()
print('*****  start section 3 - edit/append dictionary ********')
print()


#phonebook['Chris'] = '555-9876'
#phonebook['Joe'] = '555-7654'

#print(phonebook)

print()
print('*****  end section 3 ********')
print()





print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


del phonebook['Chris']

print(phonebook)

num_items = len(phonebook)

print("number of items in this list =",num_items)

myDict = {}
    #creating my own dictionary. at this point its empty, so all you have to do is add to it


print()
print('*****  end section 4 ********')
print()



'''


print()
print('*****  start section 5 - iterate through keys ********')
print()

for k in phonebook:
    print(k)
    #this prints out Chris, Katie, and Joanne. using k as the loop variable, k is the KEY
    #if you want the actual numbers in this situation, you rewrite it like so:
    #print(phonebook[k])

print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()


for v in phonebook.values():
    print(v)


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

for pair in phonebook.items():
    print(pair)
    #the output is a tuple, which is immutable
    #The output is also side by side with key and value ('Katie', '555-2222')
    #whenever they group anything together (in this example, the key and value), then the outcome is a tuple
        #this is indicated by the parenthesis() in the output \
    print(type(pair))
    #the type in this argument is to find what the datatype is of the object in question.

for k,v in phonebook.items():
    print(k)
    print(v)
    #This method iterates through both values like above but is separated by line

print()
print('*****  end section 7 ********')
print()







print()
print('*****  start section 8 - using random and converting to list ********')
print()




print()
print('*****  end section 8 ********')
print()





