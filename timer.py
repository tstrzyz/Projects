import time
import random

cur_unix_timestamp = time.time() # NOW 1342


TIMEOUT = 1


print("Please tell me (n) for n->1 countdown !!!!")
countdown_from_number = int(input())


while(countdown_from_number > 0):
	time_delta = time.time() - cur_unix_timestamp
	if( time_delta > TIMEOUT ):
		print("Countdown is at :" + str(countdown_from_number) )
		countdown_from_number -= 1;
		cur_unix_timestamp = time.time()

