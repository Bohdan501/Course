import operator
from colorama import init
from colorama import Fore, Back, Style
init()

d={'Vova' :'1990', 'Valja':'2000', 'Petro':'1994', 'Ivan':'2002'}
print ( Fore.YELLOW )
print('___________Name______________')

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
for key,z in sorted_d:
    print(key,z)


print ( Fore.CYAN )
print("___________Year_____________")
y=int(input('What a year today ? : '))

sorted_b = sorted(d.items(), key=operator.itemgetter(0))
for key1,z1 in sorted_b:
    print(z1,key1,y-int(z1),'-year')
