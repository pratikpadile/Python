#ModuleDemo1.py
#Prog to use SaiMath module and its content

'''
import SaiMath;
print(SaiMath.a);
print(SaiMath.b);
SaiMath.add(11,3);
SaiMath.sub(11,3);
SaiMath.prod(11,3);
SaiMath.div(11,3);
SaiMath.mod(11,3);
'''


'''
#Module Aliasing(alternate-name)
import SaiMath as SM;
print(SM.a);
print(SM.b);
SM.add(11,3);
SM.sub(11,3);
SM.prod(11,3);
SM.div(11,3);
SM.mod(11,3);
#print(SaiMath.a) #org-name does not work
'''


#from...import
from SaiMath import a,add,mod;
print(a);
add(11,3);
mod(11,3);
#div(11,3); 	#NameError 


'''
from SaiMath import ;	# means import-all
print(a);
print(b);
add(11,3);
sub(11,3);
prod(11,3);
div(11,3); 	#NO-Error
mod(11,3);
'''
'''
#Member-Aliasing
from SaiMath import a as x, add as sum;
print(x);
sum(11,3);
#print(a);	#NameError (Org-Name does not work)
add(11,3);	#NameError
'''