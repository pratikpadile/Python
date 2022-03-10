##Program (B.py)
##Program to define B-class & its object with diff-vars

#class-def
class B:
    '''Class-B definition'''
    def show(self):
        print("Inside show() method ::");
        print("X ::",self.x);
        print("Y ::",self.y);
        #print("Z ::",self.z);

#object-creation & usage        
obj1 = B();
print("For class-B obj1 ::");
obj1.x=10;
obj1.y=20;
obj1.z=30
obj1.show();

obj2 = B();
print("\nFor class-B obj2 ::");
obj2.x=40;
obj2.y=50;
obj2.show();