from mybox import Mybox
m=Mybox(['red','blue'])
m.add("red")
m.add("grey")
m.add("black")
print(len(m))
m.remove()
print(len(m))
print('pink' in m)

from myboxiterator import MyBoxIterator
mbi=MyBoxIterator()
next(mbi)
next(mbi)
for n in mbi:
    print(n)
    if n:
        break
