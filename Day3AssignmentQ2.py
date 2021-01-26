def swap():
    global a,b
    a,b=b,a
a=1
b=3
print("a:",a ," b",b)
swap()
print("a:",a ," b",b)