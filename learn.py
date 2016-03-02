list = ['a','b','c','d','e']
print(list[10:])
class C:
    dang=2
c1=C()
c2=C()
print(c1.dang)
c1.dang=3
print (c1.dang)
print (c2.dang)
del c1.dang
print (c1.dang)
C.dang =3
print(c2.dang)
 