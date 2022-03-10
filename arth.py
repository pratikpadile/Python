#Program to work with {} operator with format() inside print()
#sample9.py
a=11;
b=22;
add=a+b;
div=a/b;
sub=a-b
multi=a*b;
mod=a%b;
print("A =",a);
print("B =",b);

print();
print("Addition of {} and {} is = {}".format(a,b,add));
print("Division of {} and {} is = {}".format(a,b,div));
print("Substraction of {} and {} is = {}".format(a,b,sub));
print("Multiplication of {} and {} is = {}".format(a,b,multi));
print("Modulus of {} and {} is = {}".format(a,b,mod));