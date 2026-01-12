from biblioteca import *

l=liblio("central")

b1=bk("Python","Guido",1)
b2=bk("Java","Gosling",2)

l.addb(b1)
l.addb(b2)

l.show()

print(b1.prest())
print(b1.prest())
b1.ret()
print(b1.prest())
