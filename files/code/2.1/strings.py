
# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying the Intro to Programming course"
print(sentence)

# Multiline String
multiline_string = '''I am learning to code.
Python is my first programming language.
That is why I am taking this course.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am learning to code.
Python is my first programming language.
That is why I am taking this course."""
print(multiline_string)

# String Concatenation
first_name = 'Jack'
last_name = 'Wilson'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Jack Wilson
# Checking length of a string using len() builtin function
print(len(first_name))  # 4
print(len(last_name))   # 6
print(len(first_name) > len(last_name))  # False
print(len(full_name))  # 11

# Unpacking characters
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o

# Slicing

language = 'Python'
# starts at zero index and up to 3 but not include 3
first_three = language[0:3]
print(first_three)  # Pyt
last_three = language[3:6]
print(last_three)  # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2]
print(pto)  # Pto

# Escape sequence
print('I hope everyone is enjoying the course.\nAre you?')  # line break
print('Weeks\tTopics\tExercises')
print('Week 1\t3\t5')
print('Week 2\t3\t5')
print('Week 3\t3\t5')
print('Week 4\t3\t5')
print('This is a back slash  symbol (\\)')  # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

# String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'six weeks of python'
print(challenge.capitalize())  # 'Six weeks of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'six weeks of python'
print(challenge.count('o'))  # 2
print(challenge.count('o', 7, 14))  # 1
print(challenge.count('th'))  # 1

# endswith(): Checks if a string ends with a specified ending

challenge = 'six weeks of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'six\tweeks\tof\tpython'
print(challenge.expandtabs())   # 'six     weeks   of      python'
print(challenge.expandtabs(10))  # 'six       weeks     of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'six weeks of python'
print(challenge.find('e'))  # 5
print(challenge.find('th'))  # 15

# format()	formats string into nicer output
first_name = 'Jack'
last_name = 'Wilson'
job = 'student'
country = 'Australia'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(
    first_name, last_name, job, country)
print(sentence)  # I am Jack Wilson. I am a student. I live in Australia.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result)  # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'six weeks of python'
print(challenge.index('e'))  # 5
print(challenge.index('th'))  # 15

# isalnum(): Checks alphanumeric character

challenge = 'SixWeeksPython'
print(challenge.isalnum())  # True

challenge = '6WeeksPython'
print(challenge.isalnum())  # True

challenge = 'six weeks of python'
print(challenge.isalnum())  # False

challenge = 'six weeks of python 2026'
print(challenge.isalnum())  # False

# isalpha(): Checks if all characters are alphabets

challenge = 'six weeks of python'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'six weeks of python'
print(challenge.find('e'))  # 5
print(challenge.find('th'))  # 15

# isdigit(): Checks Digit Characters

challenge = 'Six'
print(challenge.isdigit())  # False
challenge = '6'
print(challenge.isdigit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal())  # True
num = '10.5'
print(num.isdecimal())  # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '6WeeksOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'six_weeks_of_python'
print(challenge.isidentifier())  # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'six weeks of python'
print(challenge.islower())  # True
challenge = 'Six weeks of python'
print(challenge.islower())  # False

# isupper(): returns if all characters are uppercase characters

challenge = 'six weeks of python'
print(challenge.isupper())  # False
challenge = 'SIX WEEKS OF PYTHON'
print(challenge.isupper())  # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' six weeks of python '
print(challenge.strip('y'))  # 5

# replace(): Replaces substring inside

challenge = 'six weeks of python'
print(challenge.replace('python', 'coding'))  # 'six weeks of coding'

# split():Splits String from Left

challenge = 'six weeks of python'
print(challenge.split())  # ['six', 'weeks', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'six weeks of python'
print(challenge.title())  # Six Weeks Of Python

# swapcase(): Checks if String Starts with the Specified String

challenge = 'six weeks of python'
print(challenge.swapcase())   # SIX WEEKS OF PYTHON
challenge = 'Six Weeks Of Python'
print(challenge.swapcase())  # sIX wEEKS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'six weeks of python'
print(challenge.startswith('six'))  # True
challenge = '6 weeks of python'
print(challenge.startswith('six'))  # False
