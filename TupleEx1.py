#Program to work with Tuple DS (TupleEx1.py)

'''
#tup1= 11,22,33,44,55;
#() are not-complusory (optional)
tup1 = (11,22,33,44,55);
print(tup1);
print(type(tup1));

#empty-tuple
tup1=();
print(tup1);
print(type(tup1));

#Tuple with Single-ValueError
tuple1(10);     #Single- Value Tuple Taken as int-values
date-type
print(tup1);
print(type(tup1));

tup1=10,;
tuple with,comma
print(tup1);
print(type(tup1));



#Other Tuple Example
#Creating Tuple with Tuple() 
list1=[11,22,33];
tup1 =tuple(list1);    
print(tup1);
tup1=tuple(range(0,20,2));   #Converts range-values to tuple
print(tup1);
tup1=tuple("hello")
print(tup1);

#Access Element with indexes
tup1=(11,22,33,44,55);
print(tup1[0]);
print(tup1[1]);
print(tup1[2]);
print(tup1[3]);
print(tup1[4]);
print();
print(tup1[-1]);
print(tup1[-2]);
print(tup1[-3]);
print(tup1[-4]);
print(tup1[-5]);
print(tup1[100]);              #IndexError
print(tup1[-100]);



#Using Slice-Opertor
tup1=(11,22,33,44,55);
print(tup1[0]);
print(tup1[1:5]);
print(tup1[0::2]);
print(tup1[0:100:2]);
print(tup1[-1:-6:-2]);



#Tuple and Immutability

tup1= (11,22,33,44,55);
print(tup1);
tup1[0]=111;                    #TypeError



#Concatenation (+)

tup1=(11,22,33);
tup2=(44,55,66);
tup3=tup1+tup2;
print(tup3);



#Tuple Repetition 
tup1=(11,22,33);
tup2=tup1*3;            #3*tup1
print(tup1)


# ***   Tuple-Functions  *** #


#len

tup1=(11,22,33);
tup1;
print(len(tup1));


#count();

tup1=(11,22,33,44,55,11,22,11);
print(tup1.count(11));
print(tup1.count(22));
print(tup1.count(55));
print(tup1.count(66));          #0 but not Error


#index()

tup1=(11,22,33,44,55,11,22,33);
print(tup1.index(11));
print(tup1.index(22));
print(tup1.index(222));         #Value error
'''

#sorted()

tup1=(11,22,33,44,11,22,11);
tup2=sorted(tup1,reverse=True);     #TRUE MEANS DESC
print(tup1);
print(tup2);