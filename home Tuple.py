animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['a']='aardvark'
animals['b']='baboon'
animals['c']='coati'
animals['d']='hiena'
print(animals)
print('_____enumerate______')

print("%1s"% "№ |","%3s"% "Key|","%1s"% 'Element ')
for n,key in enumerate(animals,1):
    print (n,'|',key,' |',animals[key])

print('_______________________________')
print(len(animals))
print('_______________________________')
input()
while True:
    n=input('print key=>')
    if n in animals:
        print(n,'=',animals[n])
    else:
        print('none key=>'+ n)











