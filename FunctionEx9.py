#Program for Anonymous Funcs or Lambda-Funcs
#Program (FunctionsEx9.py)

'''
#Prog for square of num using Lamda-Func
s = lambda n: n*n;
print("Square of 5 :",s(5));
print("Square of 9 :",s(9));
'''

'''
#Prog for sum of 3 nums using Lamda-Func
s = lambda a,b,c : a+b+c;
print("Sum of 10,20 :",s(10,20,30));
print("Sum of 11,22 :",s(11,22,33));
'''

'''
#Prog for bigger of 2 nums using Lamda-Func
s = lambda a,b : a if a>b else b;
print("Bigger of 10,20 :",s(10,20));
print("Bigger of 11,22 :",s(11,22));
'''

'''
#Prog to filter only even-nums from List using filter()
#With Lambda-Func
list1 = [11,22,33,44,55,66];
list2 = list(filter(lambda x : x%2==0,list1));
print(list2);
list2 = list(filter(lambda x : x%2!=0,list1));
print(list2);
'''


#Prog to generate sqr-nums from List using map()
'''
#With Lambda-Func
list1 = [1,2,3,4,5];
list2 = list(map(lambda x : x*x,list1));	
print(list2);
'''

'''
#reduce()
from functools import *;
list1 = [11,22,33,44,55];
result = reduce(lambda x,y:x+y, list1);
print(result);
result = reduce(lambda x,y:x*y, list1);
print(result);
'''
'''
#Sum of N-Nums
from functools import *;
result = reduce(lambda x,y:x+y, range(1,101));
print(result);
'''

'''
#Every-function is an object
def f1():
	print("Hello World");
f1();
print(f1);
print(id(f1));
'''




#function-aliasing (Same obj.ref in memory)
def f1(name):
	print("Hello :",name);
	
f2=f1;
f1("Sai");
f2("Ali")
print(f1);
print(f2);
print(id(f1));
print(id(f2));



#function-ref-deletion
def f1(uname):
	print("Hello :",uname);
	
f2=f1;
f1("Sai");
f2("Ali")
del f1;
#f1("Sai");
f2("Ali")