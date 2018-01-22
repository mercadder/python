tup2 = (1, 2, 3, 4, 5, 6, 7);  #tuplas (son inmutables: sus valores no cambian)
print "tup2[1:4]: ", tup2[1:4];
print "-"*70
print len((1,2,"a",3))  # cantidad de valores
tup3= ("a","b","c","perro","e","f","g", "i","loro");
tup4 = tup2 + tup3
print tup4
print "-"*70
tup5 = tup4[0];
tup6 = tup4[1];
suma = tup5 + tup6
cantidad = len (tup3)
print cantidad
print ("-"+"^")*40
if "loro" and "gato" in tup3:
    print tup3[2]
else:
  print tup3[0]
print "-,"*30
a = []   #lista, sus valores pueden cambiar
for x in tup2:
 L = x
 V = x*1
 if x <=5:
     a.append (x)
     print a
     print V

print "-+"*30

tup7=()
tup1=()
for i in range(1,10,3):
    tup7+= (i,)   #almacena el rango en una lista o array, += es append
print tup7

print "-"*70

print range(0, 16)

print "-.."*30

for i in range(2,10,2):   #recorre desde,hasta,step
    tup1+= (i,)
print tup1

print "._"*30

lst = []
for i in range(0,10,2):
    lst.append(i)
print "lst: ", lst
tup = tuple(lst)
print "tuple: ", tup
print "_"*30

lsta = range(1,10,2)
tupla = tuple(range(1,10,2))
tuplaLC = [i for i in range(1, 11, 3)] #list comprehension
tuplaLCif = tuple(g**2 for g in range(0, 10, 2) if g <= 6)
listaLCif = [g**2 for g in range(0, 10, 2) if g <= 6]
rrr = tuple(i for i in range(1, 10, 2))
print lsta
print tupla
print tuplaLC
print tuplaLCif
print listaLCif
print rrr
