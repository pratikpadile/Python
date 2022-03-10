#Program...(FunctionEx4.py)
#Program to demo Types of Func-Args
'''
#Positional Args
def sub(a,b):
	print(a-b);
x=11;
y=22;	
sub(x,y);	#-11
sub(y,x);	#11
sub(x,x);	#0
sub(y,y);	#0
'''

#Positional-Args with wrong output
def gross_sal(basic_sal,incentives,deductions):
    final_sal=basic_sal+incentives-deductions;
    print("Your Final-Sal ::",final_sal);

gross_sal(6500,3500,1550);
gross_sal(15000,4500,2550);
x=10000;    #basic_sal
y=3000;     #incentives
z=2000;     #deductions
gross_sal(3000,2000,1000);   #wrong-order-input
gross_sal(x,y,z);   #correct-order-input