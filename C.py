##Program (C.py)
##Program to define C-class & its object with vars & methods inside class-only

#class-def
class C:
    '''Class-C definition'''
    def __init__(self):
        #self.x=10;     #static-values
        #self.y=20;
        #self.z=30;
        self.x=int(input("Enter X value :: "));
        self.y=int(input("Enter Y value :: "));
        self.z=int(input("Enter Z value :: "));
        #self.show();
    def show(self):
        print("Inside show() method ::");
        print("X ::",self.x);
        print("Y ::",self.y);
        print("Z ::",self.z);


#object-creation & usage        
obj1 = C();
#print("For class-C obj1 ::");
obj1.show();

#obj2 = C();
#print("\nFor class-C obj2 ::");
#obj2.show();

#obj3 = C();
#print("\nFor class-C obj3 ::");
#obj3.show();
