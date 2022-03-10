#Program (FunctionEx6.py)
#Program to demo Types of Func-Args

'''
#Default-Arguments
def sum(a=11,b=3):
	print("SUM :",(a+b));
sum(10,20);
sum(100);   #b is missing(2nd-arg)
sum();      #both a,b are missing    
'''

#def sum(a=11,b):	#In-Valid (SyntaxError)
#	print("SUM :",(a+b));
def sum(a,b=3):		#Valid
    print("SUM :",(a+b));
sum(10,20);
sum(100);
sum(11);