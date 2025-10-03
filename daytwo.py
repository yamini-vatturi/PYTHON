a=10
print(type(a))
s=str(a)
print(type(s))
k=float(s)
print(type(k))

list=[1,2,3,4,5,1,2,3,4]
print(list)
rev=tuple(list)
print(rev)
h=set(list)
print(h)
h.add(9)
print(k)

dict={
    "model":"1st model",
        "year":2021,
            "age":25
}
print(type(dict))
print(dict['year'])
dict['city']='hyderabad'
print(dict)

def mom(a,b):
    print(a+b)
a=10
b=20
mom(a,b)
mom(5,6)

def mom(a,b):
    return a+b
a=10
b=20
c=mom(a,b)
print(c)
d=mom(5,6)
print(d)

