x = "There are %d types of people in this world." % 10

binary = "binary"
do_not = "don't"

y = "Those who understand %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %s." % x
print "I also said: %s" % y

hilarious = True
joke_evaluation = "Isn't that joke so funny?! %s" # This is calling a variable or string to pass after it which is called out on the line below.

print joke_evaluation % hilarious

w = "This is the left side of..."
e  = "a string with a right side."

print w + e

