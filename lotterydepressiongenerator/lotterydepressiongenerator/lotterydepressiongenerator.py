#Python lottery depression generator.
#it will show you how hard it is to simply guess a number between 1 and 292000000
#it will let you watch the eventual winner be picked via a scrol
#it will make you sad

#imports random to allow for the generators
import random


#for masochists who want to count to 292000000 choose y
#wanttowatch = raw_input('Do you want to watch it work for a winner? (y/n)  ')

##will get you those lucky lucky numbers
#feelinglucky = raw_input('do you want some winning numbers? (y/n):  ')

##to show the generated number against your guess choose y
#showmenow =raw_input('Do you want to see your guess compared to the winner (y/n):  ')

##the 1 in 292000000 chance
#bestguess = raw_input('Enter in a whole number between 1 and 292000000: ' )

#I gotta get some input to make this thing somewhat interesting
#howmany = raw_input('How many powerball tickets did you buy for the billion dollar drawing?  '  )
#carpayments = raw_input('How many car payments do you have left?  ' )
#jobhate = raw_input ('how many times have you said I hate my job today? (whole number): ')
#minutestoleave = raw_input('How many minutes would it take for you to get the hell out of town if you won the lottery:  ' )
#averageIQofatrumpvoter = raw_input('What do you think the average trump supporter has for an IQ:  ')



#test information
wanttowatch = 'n'
feelinglucky = 'y'
showmenow= 'y'
bestguess = 1234567
howmany = 2
carpayments = 3
jobhate =11
minutestoleave =6
averageIQofatrumpvoter = 50


#where I convert the input into integers
#I could have used variable = int(raw_input('stuff here') but I wanted to provide feedback as to what went wrong
try:
    
    bestguess = int(bestguess)
    bestguess <= 292000000 and bestguess > 0
except: 
    print 'You need a whole number between 1 and 292000000 what went wrong here'

try:
    int(howmany)
except:
    print 'how many powerball tickets should be a whole number'

try:
    int(carpayments)
except:
    print 'car payments should be a whole number'

try:
    int(jobhate)
except:
    print 'how much you hate your job should be a whole number'

try:
    int(minutestoleave)
except:
    print 'how many minutes it takes to leave should be a whole number'

try:
    int(averageIQofatrumpvoter)
except:
    print 'the average IQ of a trump voter should still be a whole number'

#reducing the y/n inputs into lower case
wanttowatch = wanttowatch.lower()
feelinglucky = feelinglucky.lower()
showmenow = showmenow.lower()

#the list to store the joy
powerballlist = []

def powerballpicker():
    pb =  random.randint(1,27)
    print str(pb)

powerballvar = powerballpicker

#generate that random winner
randomrandom = random.randrange(1,292000000)

def numbergenerator(inti):
    if inti <= 69:
        if inti not in powerballlist:
            powerballlist.append(inti)
    else:
        z = random.randrange(1,70)
        powerballlist.append(z)

numbergenerator(howmany)
numbergenerator(carpayments)
numbergenerator(jobhate)
numbergenerator(minutestoleave)
numbergenerator(averageIQofatrumpvoter)

def powerballvalidation():
    lenlist = len(powerballlist)
    if len(powerballlist) < 5:
        calculated = len(powerballlist)
    validation = 5-calculated
    while validation <5:
        powerballlist.append(random.randrange(1,70))
        validation + 1
    
 #sorts the list in numeric order like a powerball ticket       
powerballlist.sort()

for i in powerballlist:
    print 'power ball number' ,i
    


if showmenow == 'Y' or 'y':
    print 'The winning guess:  ' , randomrandom 
    print 'Your guess: ', bestguess
else:
    print ''


#watch and weep

if wanttowatch == 'y':
    for i in xrange(1,292000000):
        if randomrandom == bestguess:
            print 'winner winner chicken dinner'
        elif i == x:
            print 'random dude wins'
        else:
            print 'nope ' + str(i)
else:
    print 'seriously, good choice counting to 292,000,000 would be depressing as hell'