import datetime
now =   datetime.datetime.now()
print
print ("CUrrent date and timing using str method datetime object:")
print (str(now))

print 
print ("current date and time using instance attributes:")
print("Current year:%d") %now.year
print("current month:%d") %now.month
print("current date:%d")%now.date
print ("current day:%d") %now.day
