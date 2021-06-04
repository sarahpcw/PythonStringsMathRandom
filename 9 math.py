#https://docs.python.org/3.7/library/math.html

#Built-in math functions:
#Min, max, round, abs, pow

x1 = 1
x2 = 100
print (' max of 1 and 100: ', max(x1, x2) )
print (' min of 1 and 100: ', min(x1, x2) )

x , y  = 4, -4
print (abs(x) ,   abs(y))

x, y = 2, 3
print (' 2 to the power of  3 : ',pow(x, y) )
print (' 3 to the power of  2 : ',pow(y,x) )

print ( ' round to 2 decimals: ',round(123.567 , 2) )
print ( ' round to 1 decimals: ',round(123.567 , 1) )
print ( ' round to 0 decimals: ',round(123.567 , 0) )

print ( ' round to -1 units: ',round(123.567 , -1) )
print ( ' round to -1 units: ',round(127.567 , -1) )
print ( ' round to -2 units: ',round(150.567 , -2) )
print ( ' round to -2 units: ',round(144.567 , -2) )

#x rounded to n digits from the decimal point. 
#Python rounds away from zero as a tie-breaker: 
#round(0.5) is 1.0 and round(-0.5) is -1.0.

import math

print  ( ' pi: ', math.pi)
x=None
if x == None :
    print ( x)
x= math.nan
if x == math.nan:
    print ( 'nan')
print (' sqrt of 4: ', math.sqrt(x) )
print (' sqrt of 8: ', math.sqrt(8) )

print  ( ' ceil: ',math.ceil(123.567) )
print  ( ' ceil: ',math.ceil(123.123) )
print  ( ' floor:',math.floor(123.567) )
print  ( ' floor:',math.floor(123.123) )
