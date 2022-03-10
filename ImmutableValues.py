#Program to demo Immutable Values
#Program (immultableValues.py)

a= 10
print(a);
print(id(a));

a=a+10;
print(a);
print(id(a));


print();

x= 100
y= 100
print(x);
print(id(x));
print(y);
print(id(y));

print();
# is operator

a= 10;
#b= 20;
b= 20;

print(a is b);		#Checks id or address is same or not
print(id(a));
print(id(b));