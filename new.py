firstdict= {
    'model':'202',
    'name':'rog',
    'price':'$ 1899',
    
}
a=firstdict.items()
#a=firstdict.get('price')
print(a)
firstdict['color']='blue'
print(a)
if 'name' in firstdict :
    print('ok correct metti %')
    for x in firstdict.values():
     print(x)
newdict=firstdict.copy()     
b=newdict.items()
print(b)