#Program..(DictEx2.py)
#Program to Enter Student-Name and Percentage-Marks for Display in Dict-obj


records = {};	#empty-dict
n = int(input("Enter No.of Students : "));
i=1;
while i<=n:
	name=input("Enter Student Name : ");
	percentage=float(input("Enter Marks % : "));
	records[name]=percentage;
	i=i+1;

print(records);

#assigment
#Display above data in Table format(use for-loop)
