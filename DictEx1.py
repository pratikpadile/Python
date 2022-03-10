#Program (DictEx1.py)
#Program to work with Dictionary DS & its Operations

'''
#Empty-Dictionary
dict1={};       #empty-{curly-brace}
print(dict1);
print(type(dict1));
dict2=dict();   #empty-dict() function
print(dict2);
print(type(dict2));
'''

'''
#Adding Entries	dict1[key]=value;
dict1={}; 
print(dict1);
dict1[1001]="Sai";
dict1[1002]="Ram";
dict1[1003]="Ali";
print(dict1);
'''
'''
#dict{with key:values}
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1);
'''



'''
#Accessing-Data [] and keys
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(dict1[1001]);
print(dict1[1002]);
print(dict1[1003]);
print(dict1[1004]);		#KeyError
'''

#membership operator(in,not in)
dict1 = {1001:"Sai",1002:"Ram",1003:"Ali"};
print(1001 in dict1);
print(1004 in dict1);
print(1002 not in dict1);
print(1004 not in dict1);

if 1004 in dict1:
#if 1001 in dict1:
	print(dict1[1001]);
	print("Key is Found");
else:
	print("Key(1004) Not Found");





