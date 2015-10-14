# CheckDND-Lib
This library gives you a very simple object oriented API for checking DND status of any Indian mobile number.

# Example :

from DndLib import DND

obj = DND()
status = obj.check('9876543210')
if(status=='Y'):
  print "Number is registered in DND List"
elif(status=='N'):
  print "Number is NOT registered in DND List"
elif(status==1):
  print "Connection Problems"
  
