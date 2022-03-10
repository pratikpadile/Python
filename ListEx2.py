#Program
'''
#List with Dynamic Element given in [] brackets
list1=[]
print(list1);
list1=eval(input("Enter some list elements : "));
print(list1);
print(type(list1));


#Using List Conversion () & Range ()

list1= list(range(0,20,2));
print(list1);
print(type(list1));

list1=list(range(0,20,-2));
print(list1);


#Using string with list ()
ss= "pratik padile"
print(list(ss));


#Using string with split()
ss="pratik padile, avinash tigote";
list1=ss.split(" ")
print(list1);
'''

#Nasted List

list1= [11,22,33,[99,88]];
print(list1);