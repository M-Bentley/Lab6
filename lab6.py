total = 0
print "How numbers many do you want to add together?"
userInput = int(raw_input())

for x in range(userInput):
    print "Pick a number"
    userInput2 = int(raw_input())
    total = total + userInput2
print total



totaladd = []
print "How numbers many do you want to add together?"
userInput = int(raw_input())

for x in range(userInput):
    print "Pick a number"
    userInput2 = int(raw_input())
    totaladd.append(userInput2)
print "The answer is..." 
print sum(totaladd)



factorial = 1
print 'What number do you want to take the factorial of?'
userInput3 = int(raw_input())

for a in range(1, userInput3 + 1):
    factorial = factorial * a
print factorial



print 'What number do you want factors of?'
userInput4 = int(raw_input())

for b in range(1, userInput4 + 1):
    if userInput4 % b == 0:
        print b