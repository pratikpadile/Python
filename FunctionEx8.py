#Program (FunctionEx8.py)
#Program to work with Function Variables

'''
#Global-Variables
a=10;	#global-var-a
def f1():
	print(a);
def f2():
	print(a);
f1();
f2();
'''

'''
#Local-Variables
def f1():
	a=11;		#local-var-a
	print(a);
def f2():
	print(a);
def f3(a):      #arg/para as local-var-a
	print(a);

f1();
#f2();	#NameError
f3(22);
'''

'''
##sp-cases
#Both Global & Local-vars with same name
a=100;	#global-var-a(100)
def f1():
	a=11;	#local-var-a(11)
	print(a);
def f2():
	print(a); #It takes Global-Var reference

f1();
f2();
'''

'''
#global-Keyword inside a func for modifications
a=100;
def f1():
	global a;
	a=1000;		#It takes Global-Var reference
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

#f1();
#f2();

f2();
f1();
f2();
print(a);
'''


'''
#global-Keyword inside func for declaration
def f1():
	global a;
	a=100;		#It takes Global-Var reference
	print(a);
def f2():
	print(a); 	#It takes Global-Var reference

#f1();
#f2();

f2();	#NameError
f1();
'''


#Global-Var & Local-var with same-name and access both at a time
a=100;  #global-var-a=100
b=200;
c=300;
def f1():
	a=10;   #local-var-a=10		
	print(a);
	dict1 = globals();
	#print(dict1);
	print(dict1['a']);
	print(globals()['a']);
	print(globals()['b']);
	print(globals()['c']);
f1();