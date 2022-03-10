#Program (FunctionEx7.py)
#Program to demo Variable-Length Arguments

'''
#var-args
def f1(*nums):
	print(nums);
	print(type(nums));
	print("SUM :",sum(nums));	
	
f1();           #0-args
f1(11);         #1-args
f1(11,22);      #2-args    
f1(11,22,33);   #3-args
#list1 = [11,22,33,44,55];	#TypeError
#f1(list1);
'''


#Keyword with Variable-Length-Args
def f1(**nums):
	print(nums);
	print(type(nums));
	print();
    
f1(a=10,b=20,c=30);
f1(rollno=1001,name="Sai",course="CSE");