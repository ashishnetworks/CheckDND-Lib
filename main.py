from DndLib import DND
import sys

sample=DND()
v=sample.check('9876543210')
if(v=='Y'):
    print "DND Registered Number"
elif(v=='N'):
    print "DND Unregistered Number"
elif(v==1):
    print "DND Status Couldn't Get Confirmed"


