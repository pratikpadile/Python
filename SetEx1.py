#Program to work with set-ds & its Operation
#SetEx1.py


'''
#creating a set
set1={11,22,33,44,55};
set1={11,22,33,44,55,11,22,33};
print(set1);1
print(type(set1));



#using set() function
set1=set()
print(set1);
print(type(set1));
list1=[11,22,33,44,55,11,22,33];
print(list1);
set1=set(list1);
print(set1);
print(type(set1));
'''

'''
#Using range() from other collection
set1=set(range(10));
print(set1);
print(type(set1));

set1=set(range(10,20));
print(set1);
print(type(set1));

set1=set(range(20,100,5));
print(set1);
print(type(set1));

set1=set("Hello")
print(set1);
print(type(set1));
'''

'''
#Empty-Set
set1={};        #use as dict-obj
print(set1);
print(type(set1));

set1=set();     #use set()function
print(set1);
print(type(set1));
'''

# ***   SET FUNCTIONS   *** #

'''
#add

set1={11,22,33}
set1.add(55);
set1.add(56);
set1.add(57);
print(set1);
'''


'''
#Update()

set1={11,22,33}
list1=[10,20,30]
set1.update(list1);
print(set1);

set1={11,22,33}
list1=[10,20,30]
set1.update(list1,range(40,50));
print(set1);
'''

'''
#Copy()
set1={11,22,33};
set2=set1.copy();
print(set1);
print(set2);        #Order Is Not Preserved
print(id(set1));
print(id(set2));        #Here it is separate copy
'''


'''
#pop()
set1={11,22,33,44,55};
print(set1);
print(set1.pop());
print(set1.pop());
print(set1);
'''



'''
#remove(x)

set1={11,22,33,44,55};
print(set1);
set1.remove(33);
set1.remove(22);
print(set1);
set1.remove(99);        #Error Is Value is not-found
'''

'''
#discard(x)

set1={11,22,33,44,55};
set1.discard(22);
print(set1);
set1.discard(22);           #No-Error
print(set1);


#Clear()
set1={11,22,33,44,55};
print(set1);
set1.clear();
print(set1);        #Empty-Set
'''

#union on sets

set1={11,22,33,44};
set1={22,44,55,66};
print(set1.union(set2))
