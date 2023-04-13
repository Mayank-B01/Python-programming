#assigning total number of seconds
total_sec=13445

#calculating total hours

hour=int(total_sec/3600)

#calculating remaining seconds
rem_sec=total_sec-(hour*3600)

#calculating minutes
minutes=int(rem_sec/60)

#calculating seconds

second=rem_sec-(60*minutes)

#printing the total number of seconds in required format

print("13445 seconds =",hour,"hours,",minutes,"minutes, and ",second,"seconds")
