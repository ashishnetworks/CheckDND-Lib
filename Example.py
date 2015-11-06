from CheckDnd import DND
import sys

sample=DND()

if len(sys.argv)>=2:
  v=sample.check(sys.argv[1])
else:
  v=sample.check('9876543210')

if(v=='Y'):
    print "DND Registered Number"
elif(v=='N'):
    print "DND Unregistered Number"
elif(v==1):
    print "DND Status Couldn't Get Confirmed"


