#https://docs.python.org/2.4/lib/string-methods.html

#More String Functions: Strip, Lstrip, Rstrip

fb = '  foobar  '
print ("  strip :",fb.strip(),"removes both  leading and trailing spaces")
print (" lstrip :",fb.lstrip(),"removes only  leading   spaces ")
print (" rstrip :",fb.rstrip(),"removes only  trailing spaces ")

#More String Functions: Title, Lower, Upper, Swapcase
str="flowers guns and roses"  
print (" titlecase : ",str.title() ) # every word capitalsed
print (" swap case : ",str.capitalize(), 'the original is ', str )  # only first word capitalsed
print (" lowercase : ",str.lower())
print (" uppercase : ",str.upper() )
print (" swap case : ",str.swapcase(), 'the original is ', str )

#Exercise: Movies Program : Title Case (Or Lower Case)
#
#Change the movie program: 
#•	Update the list to keep all the movies in Title case (can you do this using a for-loop)
#•	If the enduser replies, change the reply to title case
#o	Then look for the movie in the list for the movie
#
#
#String Function:  Len
str = "John"
print(len(str))

str = "Peter"
print(len(str))

str = "dumb and dumber"
print(len(str))


#String Function: Count
str = "dumb and dumber"		# counts how many times is dumb in ‘dumb and dumber’
print (str.count('dumb') )
print (str.count('dumb', 0 ))		# start index  
print (str.count('dumb', 0, 5  ))		# start index and end index
print (str.count('dumb', 5, len(str)  ))	# start index and end index
print (str.count('dumb', 5 ))	# start index and end index

#String Functions:  Concatenate

#concat --  
color =  'red'+'yellow'
print (color)

#String Functions:  Replace
str = "The American Werewolf"
str = str.replace ("Werewolf","Beauty")
print (str)

str = "Dumb and Dumber"
str = str.replace ("Dumb","Cool")
print (str)


#String Functions:  Split
#example
str = "dumb and dumb er"
mylist = str.split(' ') 				# split creates an array of values separated by spaces
print (len(mylist))
print ( mylist )
print ( mylist[0] )
print ( mylist[1] )
print ( mylist[2] )

#example
str = "dumb and dumber"
b = str.split(' ') 				# split creates an array of values separated by spaces
for each in range(0,len(b),1) :
	print (b[each])

print(' '.join(b))   # putting it together again

numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))






#Exercise

adults = 2
line = 'schrek,mon,10.0,action'		
mylist = line.split(',') 				# split creates an array of values separated by spaces
print (len(mylist))
print ( "movie ticket price is " , adults * float ( mylist[2]) )

# split creates an array of values separated by commas
#•	what must 2 adults pay to see the movie?


#Exercise Join and split
#Join and split exercise 
#
#Your are giving a string with spaces: 
#“This is a string “
#You have to split it by spaces and join it again with hyphens:
#“This-is-a-string”



#String Function: Substring
word= "flowers, rose, sunshine"
print ( word[0:3] )     	   # substrIng the first 3 characters
print ( word[0:7] )    	   # substrIng the first 7 characters
print ( word[9:13] )     	   # substrIng from position 9 to 13
x  =  word[0:3]
print(x)


#String Function: Find
#Returns the position where the string was found and -1 (negative )if not found
str= "flowers, rose, sunshine"
str2 = "x";
print ("where is the s? start looking at position  0 ",str.find(str2))


startLooking = str.find(str2)+1
stopLooking = len(str)
print ("where is the s? ", str.find(str2, startLooking, stopLooking ))


startlooking = str.find(str2, startLooking,stopLooking )
#print ("where is the s? “, str.find(str2, startlooking) ) 


#String Functions: Find, Count
#Example: loop to show all positions of str2 within str
str= "flowers, rose, sunshine"
str2 = "s";
startLooking = 0

if str.startswith(str2): 
    print (" index ",str.find(str2, 0))

while ( startLooking >=0 ): 
    startLooking =  startLooking + 1
    startLooking = str.find(str2, startLooking ) 
    if startLooking >=0:
        	print ( " index " , startLooking )
#Example: loop to show all positions of str2 within str
c = 0
x = 0
while ( c <= str.count(str2)  ): 
    if str.find(str2, x ) > -1 : 
        print ( str.find(str2, x ) )
    x = str.find(str2, x ) + len(str2) +1
    c += 1
#String Functions: Find, Count
mTitle = "dumb and dumber"
#              "012345678901234" 
print ("dumb is at position : ", mTitle.find("dumb",0) )
print ("dumb is at position : ", mTitle.find("dumb",3) ) 

count = mTitle.count('dumb')
print (" dumb is found " , count , "times")
print (" dumb is found " , mTitle.count('dumb') , "times")

count = mTitle.count('dumb')
x = 0
if (count > 0):
for each in range ( count ):
        x = mTitle.find('dumb', x)
        print (' found at : ' , x)
        x = x + 1
else:
	print ('not found')
String Function - Startswith, Endwith
if str.startswith("dumb"):   # Check how a string starts
print("String starts with 'Dumb'. Good!")

if str.endswith("ber"): # Check how a string ends
print("String ends with 'ber!'. Good!")      
