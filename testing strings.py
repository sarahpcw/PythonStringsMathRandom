from datetime import datetime

adults = 2
line = 'schrek,mon,10,action'		# split creates an array of values separated by commas
#•	what must 2 adults pay to see the movie?

b = line.split(',')
price = float(b[2])
price = int(  b[2]  )
print ( b[2], type ( price), price)
ticketprice = adults * price
print ( adults, price, ticketprice)


filename= 'C:\\Users\\u\\Desktop\\python tab delimited txt file.txt'
myfile = open(filename,'r') 
for line in myfile:
    line = line.replace('\n','')
    b = line.split('\t')
    price= float ( b[2].replace('"','').replace(',','.') ) 
    print ( price , type(price) )
    ticketprice = adults * price
    print ( adults, price, ticketprice)
    myStringDate = b[6]
    print ( 'myStringDate', type (myStringDate))
    mydate = datetime.strptime(myStringDate,'%m/%d/%Y')
    print ( 'mydate', type (mydate), mydate)
myfile.close()
#
mydate = datetime.strptime(myStringDate,'%m/%d/%Y') #convert string todaye
print ( mydate.strftime('%Y-%m-%d') ) #convert date to string for printing

print ( mydate.strftime('%Y-%B-%d %A %W %z %Z %j ') )
print ( '%c %X', mydate.strftime('%c %X'))
print ( '%Z Timezone', mydate.strftime('%Z') )

print ( mydate.year, type( mydate.year )) # return integer
print ( mydate.month) # integer
print ( mydate.day)   # integer

print (datetime.today().strftime('%z')) #datetime 


import time
print ( time.time() )
print ( time.localtime())
print (time.asctime(time.localtime()))


print ( time.timezone ) 
#The offset of the local (non-DST) timezone, in seconds west of UTC (negative in most of Western Europe, positive in the US, zero in the UK).

print ( time.tzname )
#A tuple of two strings: the first is the name of the local non-DST timezone, the second is the name of the local DST timezone. If no DST timezone is defined, the second string should not be used.

#print ( time.tzset() )

