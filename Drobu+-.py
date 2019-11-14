from math import gcd
#29/30+44/45=35/18

n1=int(input("чисельник 1-го числа"))
d1=int(input("знаменник 1-го числа"))
n2=int(input("чисельник 2-го числа"))
d2=int(input("знаменник 2-го числа"))

if d1 == d2:
    print('{}/{}'.format(n1 + n2, d1))
else:
    cd = int(d1 * d2 / gcd(d1, d2))

    rn = int(cd / d1 * n1 + cd / d2 * n2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print("Результат додавання дробів:")
    print('{}/{}'.format(n, d) if n != d else n)



if d1 == d2:
    print('{}/{}'.format(n1 - n2, d1))
else:
    cd = int(d1 * d2 / gcd(d1, d2))

    rn = int(cd / d1 * n1 - cd / d2 * n2)
    g2 = gcd(rn, cd)
    n = int(rn / g2)
    d = int(cd / g2)
    print("Результат віднімання дробів:")
    print('{}/{}'.format(n, d) if n != d else n)






