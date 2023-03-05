
 #RegEx
#Q1) Detect Floating Point Number
import re 
n = int(input())

pattern = r'^[+-]?[0-9]*\.[0-9]+$'

for i in range(n):
    s = input()
    print(bool(re.match(pattern, s)))


# # Q2)  Re.split()


regex_pattern = r"[,.]+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


# # Q3) Group(), Groups() & Groupdict()
import re

a = input()
pattern = r'([a-z A-Z 0-9])\1'
b = re.search(pattern, a)
if b:
    print(b.groups()[0])
else:
    print(-1)


# # Q4) Re.findall() & Re.finditer()

import re

a = input()

v = "aeiou"
c = "qwrtyupsdfghjklzxcybnm"
l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), a, flags=re.IGNORECASE)
#print("\n".join(l or -1))

if not l:
    print(-1)
else:
    for i in l:
        print(i)


# # Q5) Re.start() & Re.end()


import re

s = input()
k = input()

pattern = re.compile(k)
m = pattern.search(s)

if not m:
    print("(-1, -1)")
else:
    while m:
        print("({0}, {1})".format(m.start(), m.end() -1))
        m = pattern.search(s, m.start() + 1)


# # Q6) Regex Substitution


import re

pattern = r"(?<= )(&&|\|\|)(?= )"

replacement = lambda x: "and" if x.group() == "&&" else "or"

for i in range(int(input())):
    s = input()
    print(re.sub(pattern, replacement, s))


# # Q7) Validating Roman Numerals


thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)


import re
print(str(bool(re.match(regex_pattern, input()))))


# # Q8) Validating and Parsing Email Addresses

import re

N = int(input())

for i in range(N):
    name, email = input().split()
    pattern="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(pattern, email)):
        print(name,email)


# # Q9) Hex Color Code

import re

n = int(input())
in_css = False
for i in range(n):
    s = input()
    if '{' in s:
        in_css = True
    elif '}' in s:
        in_css = False
    elif in_css:
        for color in re.findall('#[0-9a-fA-F]{3,6}', s):
            print(color)


# # Q10) HTML Parser - Part 1

from html.parser import HTMLParser

N = int(input())
class MyHTMLParser(HTMLParser): # Subclass
    
    def handle_starttag(self, tag, attributes):
        print('Start :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
    def handle_endtag(self, tag):
        print('End   :', tag)
        
    def handle_startendtag(self, tag, attributes):
        print('Empty :', tag)
        for element in attributes:
            print('->', element[0], '>', element[1])
            
Parser = MyHTMLParser()
Parser.feed(''.join([input().strip() for i in range(0, N)]))


# # Q11) HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # HTML Parser - Part 2 in Python - Hacker Rank Solution START
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data.replace("\r", "\n"))
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
    # HTML Parser - Part 2 in Python - Hacker Rank Solution END
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# # Q12) Detect HTML Tags, Attributes and Attribute Value


# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

# Same approach as the HTML Parser 1 Challenge! Make a subclass and override methods
N = int(input())
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attributes):
        print(tag)
        [print('-> {} > {}'.format(*attribute)) for attribute in attributes]
    
html = '\n'.join([input() for x in range(0, N)])  
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# # Q13) Validating UID


n = int(input())

for i in range(n):
    a = str(input())
    c = 0
    for i in a:
        if(i.isupper):
            c+=1
    if (c>1):
        d=0
        for j in a:
            if(j.isnumeric()):
                d+=1
        if(d>2):
            if(a.isalnum()):
                if(len(a)==10):
                    t=0
                    for k in a:
                        for h in a:
                            if(k==h):
                                t+=1
                    if(t==10):
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")


# # Q14) Validation Credit Card Numbers



import re

for _ in range(int(input())):
    num = input()

    ok1 = bool(re.match(r"^[456]\d{15}$", num))
    ok2 = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", num))
    num = num.replace("-", "")
    ok3 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
    if (ok1 or ok2) and ok3:
        print("Valid")
    else:
        print("Invalid")


# # Q15) Validating Postal Codes


regex_integer_in_range = r"^[1-9]\d{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# # 16) Matrix Script



import math
import os
import random
import re
import sys



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded_message = ""
for column in range(m):
    for row in range(n):
        decoded_message += matrix[row][column]        

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", decoded_message))


# # 17) Validating Phone Numbers


import re 

def checker(contact):
    pattern = r"[789]\d{9}$"
    if re.match(pattern, contact):
        return "YES"
    else:
        return "NO"
    
    
a = int(input())

for i in range(a):
    print(checker(input()))




