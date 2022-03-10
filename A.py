##Program (A.py)
##Program to define Student-class & its object

#class-def
class A:
    '''Class-A definition'''
    def show(self):
        print("Inside show() method ::");
        print("X ::",self.x);
        print("Y ::",self.y);

#object-creation & usage        
obj1 = A();
print("For class-A obj1 ::");
obj1.x=10;
obj1.y=20;
obj1.show();

obj2 = A();
print("\nFor class-A obj2 ::");
obj2.x=30;
obj2.y=40;
obj2.show();