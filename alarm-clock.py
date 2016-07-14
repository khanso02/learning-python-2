import winsound
import time
starttime=time.time()
def alarm():
	print "alarm"

def timer():
	hours = int(raw_input("Enter the amount of hours"))
	minutes = int(raw_input("enter the amount of minutes"))
	seconds = int(raw_input("Enter the amount of seconds"))
	
	h= hours*60*60
	m= minutes*60
	s= seconds
	
	n = h + m + s
	
	while n > 0:
		n=n-1
		print n
		time.sleep(1)
	if n == 0:
		n=n-1
		print "ding!"
		winsound.Beep(300,500)
	while n < 0:
		timer()
		
	
choice = raw_input('Press 1 for timer. Press 2 for alarm:')
timer()

if choice in [1]:
	timer()
elif choice in [2]:
	alarm()
	
