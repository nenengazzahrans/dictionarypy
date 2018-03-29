a = {'Jane Doe' : '+27 555 5367','John Smith': '+27 555 6254','Bob Stone' : '+27 555 5689'}
a['Jane Doe'] = '+27 555 1024'
a['Anna Cooper'] = '+27 555 3237'
a.keys()
a.values()
print("Bob Stone : ", a['Bob Stone'])
for keys in a.keys() :
    print (keys)
for values in a.values() :
    print (values)
