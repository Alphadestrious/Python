



def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

        
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


def any_lowercase5(s):
    for i in s:
        if not i.islower():
            return False
    return True


print any_lowercase1('Ab')
print any_lowercase2('Ab')
print any_lowercase3('Ab')
print any_lowercase4('Ab')
print any_lowercase5('Ab')


#The reason why the functions will not run correctly with an empty string ''
#is because it requires a string to check if it is lowercase or not, which returns the value true or false.
#Integer will not pass because there is nothing in the string it pass or iterate. There are no letters.


#dictionaries, this will also demonstrate "counting" and keeping track of the
#counts 

def create_histogram(sentance):
    wordCount_dictionary = dict()
    for letter in sentance:
        if letter not in wordCount_dictionary:
            wordCount_dictionary[letter]=1
        else:
            wordCount_dictionary[letter] += 1
    return wordCount_dictionary

def print_histogram(h):
    for letter in h:
        if letter !='':
            print letter, 'appears', h[letter], 'times'



h = create_histogram('UniversityofTexasatElPaso')
print "The dictionary containing histogram:"
print h
print_histogram(h)





