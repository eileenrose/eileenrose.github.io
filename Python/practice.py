

# Hi - I am a comment.
print "My name is Eileen"   # This is line 2
print "What is your name?"
# oh boyy
# i guess there's no multi comment line
# like /**/ for java(script)
# thus we have to manually # every line :/
minion = "Kevin"
print minion
print minion
minion = "Carl"
print minion

despicable_me = "Gru"
print despicable_me

a = 25
b = 36
print a * b

dog = "Ralph"
cat = "Whiskers"
print dog + " loves " + cat


first = "BARACK"
last = "OBAMA"
age = 53
print "The president is: " + first.capitalize() + \
" " + last.lower()
#capitalizes the first character then lowercases the rest
#lower turns into all lowercase, upper turns into uppercase
# \ continues onto next line because spacing is actually important in python

name = "Bill"
age = 16
print "Name: " + name + " Age: " + str(age)
# age = str(age) converts age into string, but otherwise does not convert
print type(age)

left_number = raw_input("Enter a number: ")
right_number = raw_input("Enter another number: ")
#always converted into string, so convert to number, do calcs, then to string
if not left_number.isdigit() or not right_number.isdigit():
    print "Bad input! Please enter an integer."
    exit(1)
print "The sum is: " + str(int(left_number) + int(right_number))

mehFirst = raw_input("First name? ")
mehLast = raw_input("Last name? ")
print "Your name is: " +mehFirst + " " + mehLast

from random import randrange, uniform
guessUser = raw_input("Pick a number from 1 to 10: ")
irand = str(randrange(1,10))
print "The number was " + irand
if (guessUser == irand):
    print "You guessed right!"
else:
    print "You lost."

phone_number = raw_input("What is your phone number? ")
if len(phone_number) != 13:
    print "Bad format, wrong length."
    exit(1)
if phone_number[0] != "(" or phone_number[4] != ")":
    print "Bad format, area code not encased in parentheses."
    exit(1)
if not phone_number[1:4].isdigit() or not phone_number[5:8].isdigit() or not phone_number[9:].isdigit():
    print "Bad format, not numbers"
    exit(1)
if phone_number[8] != "-":
    print "Bad format, no dash"
    exit(1)
print "Your phone number is valid."

for i in range(1, 10):
    print i

for j in range(1, 10, 2):
    print j

count = 1
while count < 10:
    print count
    count += 1 ##   i++ notation does not work
else:
    print "count is "+ str(count)
students = ["Gaby", "John","Larry", "Sergey", "Jose"]
if "Sergey" in students:
    print "Welcome Gaby!"
else:
    print "Where is Sergey?"

for student in students[2::2]:
    print "Student: " + student

numbers = [2, 52, 19, 46, 1000]

for num in numbers:
    num = (num + 10) / 2
    print num

presidents = ["George", "John", "Thomas", "James", "John Quincy"]

for pre in presidents[::-1]:
    print pre

for pre in reversed(presidents):
    print pre

n2 = -1
while n2 > -6:
    print presidents[n2]
    n2 -= 1

fruit = raw_input("What is your favoirte fruit? ").lower().strip()
myfruit = "apple"
if (fruit == myfruit):
    print "Me too."

age = raw_input("How old are you? ")
years = 18
print "You will be {age} in {years} years.".format(age = int(age)+years, years = years)

fav = raw_input("What is your favorite food? ")
fav = fav.upper()
vowels = ["A", "E", "I", "O", "U"]
for v in vowels:
    fav = fav.replace(v, v*3)
print fav
