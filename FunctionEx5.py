###Program (FunctionEx5.py)
#Program to demo Types of Func-Args with Keyword-Args

def f1(uname,msg):
	print("Hello :",uname,msg);
	
f1(uname="Sai",msg="Thank You!!");
f1(msg="All the Best",uname="Ram");

#both postion-args & keywords-args
f1("Ali",msg="Hava a nice day");
#f1(uname="Tom","All the Best");	#InValid (SyntaxError)