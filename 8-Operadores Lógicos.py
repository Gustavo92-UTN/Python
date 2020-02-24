'''
Operadores logicos
Negacion:           not
And (conjuncion):   and
Or (disyuncion):    or
'''
a=10
b=12
c=13
d=10
resultado=((a>b)or(a<c))and((a==c)or(a>=b)) #Para los operadores logicos, se le da prioridad al NOT, luego AND y por
print(resultado)                            #ultimo al OR

a=10
b=15
c=20
resultado=not((a>=b)and(c!=a)or(not(b==c)))
print(resultado)