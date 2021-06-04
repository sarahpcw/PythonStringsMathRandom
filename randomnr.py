import random

nr = random.randint(0,2)
print ( nr )

movies = [  'bambi', 'rambo', 'schrek', 'cinderella', 'scarface']
days = ['mon', 'tue', 'wed' , 'sat','sun']

usernr = input('Guess a number between 0 and 2 inclusive? ' )
usernr = int(usernr)
print ( usernr)
if nr == usernr: 
    print ( 'Congratulations , you won a movie ticket:', movies[nr],'showing on',days[nr] )
else: 
    print ( 'bad luck, you did not win anything')