##Program (D.py)
##Program to define D-class & its object with vars & methods outside the class

#class-def
class D:
    '''Class-D definition'''
    
#object-creation & usage        
obj1 = D();
obj1.x=10;
obj1.y=20;
print("For class-D obj1 ::");
print("X ::",obj1.x);
print("Y ::",obj1.y);

obj2 = D();
obj2.x=100;
obj2.y=200;
obj2.z=300;
print("For class-D obj2 ::");
print("X ::",obj2.x);
print("Y ::",obj2.y);
print("Z ::",obj2.z);

obj3 = D();
obj3.x=1000;
obj3.y=2000;
obj3.z=3000;
obj3.p=4000;
print("For class-D obj3 ::");
print("X ::",obj3.x);
print("Y ::",obj3.y);
print("Z ::",obj3.z);
print("P ::",obj3.p);