#Program...(FunctionEx3.py)
#Program to define a function with return value
'''
def sum(a,b):
	return (a+b);
	
x=11;
y=22;	
c = sum(x,y);
print("SUM1 :",c);
c = sum(111,222);
print("SUM2 :",c);
print("SUM3 :",sum(1111,2222));	#using or calling a func in print() para
'''


#Multiple-return values (Arithmetic-Opertions)
def calci(a,b):
	add=a+b;
	sub=a-b;
	prod=a*b;
	div=a/b;
	mod=a%b;
	return (add,sub,prod,div,mod);
tup1 = calci(11,3);
print(tup1);
print(type(tup1));
print("\nResult(using-loop) :");
for x in tup1:
	print(x);