#Program to work with list data structure
#Program (ListEx1.py)

'''
#using Indexes

list1= [54,64,74,84,94];
print(list1[0]);
print(list1[1]);
print(list1[2]);
print(list1[3]);
print(list1[4]);
print();
print(list1[-1]);
print(list1[-2]);
print(list1[-3]);
print(list1[-4]);
print(list1[10]);       #Index error: List index Out Of the range.

print();

#Using Slice-Operator

list1= [11,22,33,44,55,66,77,88,99,110];
print(list1);
print(list1[2:7:2]);
print(list1[4::2]);
print(list1[1:6:1]);
print(list1[4:100]);       #No Error (For 100) but take till last index


print();

#List iS Mutable (Original Data Can Be Modified)

list1=[11,22,33,44,55];
print(list1);
list1[1]=222;
print(list1);
'''

#List using for-loops:

list1= [11,22,33,44,55,66,77];
for x in list1:
    print(x);

print();

#List Using While-loops:

i=0;
while i<len(list1):
    print(list1[i]);
    i=i+1;