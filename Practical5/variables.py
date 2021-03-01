a = 270502
b = 190784
c = 100321

d = abs(a - c)
e = abs(a - b)

if d > e:
    print( "d is larger")
elif d == e:
    print( "they are equal")
else:
     print( " e is larger")

x = True
y = False
z = (x	and	not	y)	or	(y	and	not	x)
print( " when x=", str(x), "y = ", str(y) )
if z:
    print("z is true")
w = x!=y
if w == z:
    print("both w and z are true")

x = True
y = True
z = (x	and	not	y)	or	(y	and	not	x)
print( " when x=", str(x), "y = ", str(y) )
if z:
    print("z is true")
w = x!=y
if w == z:
    print("both w and z are true")

x = False
y = False
z = (x	and	not	y)	or	(y	and	not	x)
print( " when x=", str(x), "y = ", str(y) )
if z:
    print("z is true")
w = x!=y
if w == z:
    print("both w and z are true")

x = False
y = True
z = (x	and	not	y)	or	(y	and	not	x)
print( " when x=", str(x), "y = ", str(y) )
if z:
    print("z is true")
w = x!=y
if w == z:
    print("both w and z are true")
