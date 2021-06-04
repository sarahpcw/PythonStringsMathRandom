import random 
 
# First random number
print ("random(): ", random.random() )  # returns float between 0 and 1 

print (random.uniform(2.5, 3.5))             # returns float within a range 



print ('randint(0,100):',random.randint(1, 6)) # returns integer  within a range

print ('choice(range(...)) :',random.choice(range(0,9,1))) # returns integer within a range



print ("choice([1, 2, 6, 5, 13]) : ", random.choice([1, 2, 6, 5, 13])) # returns integer from a list

#returns a random letter from a string ’
print ("choice('A String') : ", random.choice('abcdefgh'))	# returns a string from a list
