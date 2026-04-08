classes_doc = '''Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
num = 1
numstr = ''
while num > 0:
    if num // 1000 > 0:
        last3 = str(num % 1000).zfill(3)
    else:
        last3 = str(num % 1000)
    num = num // 1000
    if numstr != '':
        numstr = last3 + ',' + numstr
    else:
        numstr = last3 + numstr

    
num
0
numstr
'1'
help()
modules
symbols
<<
topics
CLASSES        
print
keywords
lambda 
nonlocal 
await
raise
quit

try:
    print(1 / 0)
except:
    raise RuntimeError("Something bad happened")

Traceback (most recent call last):
  File "<pyshell#8>", line 2, in <module>
    print(1 / 0)
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 4, in <module>
    raise RuntimeError("Something bad happened")
RuntimeError: Something bad happened
try:
    print(1 / 0)
except:
    print('No)
          
SyntaxError: unterminated string literal (detected at line 4)
try:
    print(1 / 0)
except:
    print('No')

    
No
def check_day(day):
    try:
        if day > 31:
            raise ValueError('This day is way too much.')
        if '.' in str(day):
            raise TypeError('I am so sorry, you have fractional days.')
        if day < 1:
            raise ValueError('This day is way too little.')
    except (ValueError, TypeError) as msg:
        print('Your day is invalid because of a', msg)

        
check_day(1234)
Your day is invalid because of a This day is way too much.
def check_day(day):
    try:
        if day > 31:
            raise ValueError('This day is way too much.')
        if '.' in str(day):
            raise TypeError('I am so sorry, you have fractional days.')
        if day < 1:
            raise ValueError('This day is way too little.')
    except (ValueError, TypeError) as msg:
        print('Your day is invalid. My program says:', msg)

        
check_day(1.3)
Your day is invalid. My program says: I am so sorry, you have fractional days.
check_day(-34598437294765284956729347519347583475)
Your day is invalid. My program says: This day is way too little.
check_day(2)
def check_day(day):
    try:
        if day > 31:
            raise ValueError('This day is way too much.')
        elif '.' in str(day):
            raise TypeError('I am so sorry, you have fractional days.')
        elif day < 1:
            raise ValueError('This day is way too little.')
        else:
            print('Your day is fine. Thanks!')
    except (ValueError, TypeError) as msg:
        print('Your day is invalid. My program says:', msg)

        
check_day(31)
Your day is fine. Thanks!
'                       hi    '.strip()
'hi'
'rkhirgoisjrhilzdfgliehblifghjslihxlighlihfkjgharligxdfligherlbijsrehqpbkxsufgblierugbhgxg'.replace('g', '_._')
'rkhir_._oisjrhilzdf_._liehblif_._hjslihxli_._hlihfkj_._harli_._xdfli_._herlbijsrehqpbkxsuf_._blieru_._bh_._x_._'
file = open('nothing.txt', 'w')
file.write('ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
77
print(file.name)
nothing.txt
file.close()
file
<_io.TextIOWrapper name='nothing.txt' mode='w' encoding='cp1252'>
help()
pygame


You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
class Asteroid:
    \''' Whatever you think this class does.\'''
    count = 0
    def __init__(self, size, material):
        Asteroid.count += 1
        self.size = size
        self.substance = material
    def see():
        return self.size, self.substance
    def explode():
        energy = size * 100
        return energy

    
Pluto = Asteroid(167, iron)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    Pluto = Asteroid(167, iron)
NameError: name 'iron' is not defined
Pluto = Asteroid(167, 'iron')
print(Pluto.see())
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(Pluto.see())
TypeError: Asteroid.see() takes 0 positional arguments but 1 was given
print(Pluto.see())
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(Pluto.see())
TypeError: Asteroid.see() takes 0 positional arguments but 1 was given
class Asteroid:
    \''' Whatever you think this class does.\'''
    count = 0
    def __init__(self, size, material):
        Asteroid.count += 1
        self.size = size
        self.substance = material
    def see(self):
        return self.size, self.substance
    def explode(self):
        energy = size * 100
        return energy

    
Pluto = Asteroid(167, 'iron')
print(Pluto.see())
(167, 'iron')
Pluto.explode()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    Pluto.explode()
  File "<pyshell#59>", line 11, in explode
    energy = size * 100
NameError: name 'size' is not defined. Did you mean: 'self.size'?
class Asteroid:
    \''' Whatever you think this class does.\'''
    count = 0
    def __init__(self, size, material):
        Asteroid.count += 1
        self.size = size
        self.substance = material
    def see(self):
        return self.size, self.substance
    def explode(self):
        energy = self.size * 100
        return energy

    
Pluto = Asteroid(167, 'iron')
print(Pluto.see())
(167, 'iron')
Pluto.explode()
16700
Pluto.see()
(167, 'iron')
help(str)

print(Asteroid.count)
1
from math import sqrt
class Comet(Asteroid):
    def burnup_time(self, atmosphere): #atmosphere is in km
        time = atmosphere - (sqrt(self.size) * 3)\
        return time
    
SyntaxError: invalid syntax
class Comet(Asteroid):
    def burnup_time(self, atmosphere): #atmosphere is in km
        time = atmosphere - (sqrt(self.size) * 3)
        return time

    
Halley = Comet(12, 'ice')
burnup_time(Halley)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    burnup_time(Halley)
NameError: name 'burnup_time' is not defined
Halley.burnup_time(5)
-5.392304845413264
class Comet(Asteroid):
    def burnup_time(self, atmosphere): #atmosphere is in km
        time = atmosphere - (sqrt(self.size) * 3)
        if time < 0:
            return 'The comet explodes.'
        else:
            return time

        
Halley = Comet(12, 'ice')
Halley.burnup_time(5)
'The comet explodes.'
Halley.burnup_time(13)
2.607695154586736
Pluto
<__main__.Asteroid object at 0x000001D0DD0616A0>
type(Pluto)
<class '__main__.Asteroid'>
type(Halley)
<class '__main__.Comet'>
burnup_time(Halley)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    burnup_time(Halley)
NameError: name 'burnup_time' is not defined
Halley.size
12
>>> class Telescope:
...     \''' Whatever in the universe
...             you think this dummy class does!!!!!!!!!!!!!!!!!!!!!!!!!!!\'''
...     def __init__(self, length, radius):
...         self.length = length
...         self.radius = radius
...         self.seeing_area = radius * radius * 3.142
...     def see(self):
...         return self.length, self.radius, self.seeing_area
... 
...     
>>> thing thing = 2
SyntaxError: invalid syntax
>>> HubbleSpace = Telescope(123, 56)
>>> see(HubbleSpace)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    see(HubbleSpace)
NameError: name 'see' is not defined. Did you mean: 'set'?
>>> HubbleSpace.see()
(123, 56, 9853.312)
>>> def general_see(object):
...     see(object)
... 
...     
>>> KeppleIsland = Asteroid(676, 'dirt')
>>> general_see(KeppleIsland)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    general_see(KeppleIsland)
  File "<pyshell#108>", line 2, in general_see
    see(object)
NameError: name 'see' is not defined. Did you mean: 'set'?
>>> def general_see(object):
...     object.see()
... 
...     
>>> general_see(KeppleIsland)
>>> print(general_see(KeppleIsland))
None
>>>
#Please Remember To Treat Object Functions And Normal Functions Sepeartely!!!!!!!!!!!!\
'''

patterns_doc = '''Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import re
help(re)

The special characters are:
        "."      Matches any character except a newline.
        "^"      Matches the start of the string.
        "$"      Matches the end of the string or just before the newline at
                 the end of the string.
        "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
                 Greedy means that it will match as many repetitions as possible.
        "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
        "?"      Matches 0 or 1 (greedy) of the preceding RE.
        *?,+?,?? Non-greedy versions of the previous three special characters.
        {m,n}    Matches from m to n repetitions of the preceding RE.
        {m,n}?   Non-greedy version of the above.
        "\\"     Either escapes special characters or signals a special sequence.
        []       Indicates a set of characters.
                 A "^" as the first character indicates a complementing set.
        "|"      A|B, creates an RE that will match either A or B.
        (...)    Matches the RE inside the parentheses.
                 The contents can be retrieved or matched later in the string.
        (?aiLmsux) The letters set the corresponding flags defined below.
        (?:...)  Non-grouping version of regular parentheses.
        (?P<name>...) The substring matched by the group is accessible by name.
        (?P=name)     Matches the text matched earlier by the group named name.
        (?#...)  A comment; ignored.
        (?=...)  Matches if ... matches next, but doesn't consume the string.
        (?!...)  Matches if ... doesn't match next.
        (?<=...) Matches if preceded by ... (must be fixed length).
        (?<!...) Matches if not preceded by ... (must be fixed length).
        (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                           the (optional) no pattern otherwise.

    The special sequences consist of "\\" and a character from the list
    below.  If the ordinary character is not on the list, then the
    resulting RE will match the second character.
        \number  Matches the contents of the group of the same number.
        \A       Matches only at the start of the string.
        \Z       Matches only at the end of the string.
        \b       Matches the empty string, but only at the start or end of a word.
        \B       Matches the empty string, but not at the start or end of a word.
        \d       Matches any decimal digit; equivalent to the set [0-9] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode digits.
        \D       Matches any non-digit character; equivalent to [^\d].
        \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
                 bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the whole
                 range of Unicode whitespace characters.
        \S       Matches any non-whitespace character; equivalent to [^\s].
        \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
                 in bytes patterns or string patterns with the ASCII flag.
                 In string patterns without the ASCII flag, it will match the
                 range of Unicode alphanumeric characters (letters plus digits
                 plus underscore).
                 With LOCALE, it will match the set [0-9_] plus characters defined
                 as letters for the current locale.
        \W       Matches the complement of \w.
        \\       Matches a literal backslash.

    This module exports the following functions:
        match     Match a regular expression pattern to the beginning of a string.
        fullmatch Match a regular expression pattern to all of a string.
        search    Search a string for the presence of a pattern.
        sub       Substitute occurrences of a pattern found in a string.
        subn      Same as sub, but also return the number of substitutions made.
        split     Split a string by the occurrences of a pattern.
        findall   Find all occurrences of a pattern in a string.
        finditer  Return an iterator yielding a Match object for each match.
...         compile   Compile a pattern into a Pattern object.
...         purge     Clear the regular expression cache.
...         escape    Backslash all non-alphanumerics in a string.
...         

>>> re.search('.*', 'blkepppeoikjsihhjjhfuu')
<re.Match object; span=(0, 22), match='blkepppeoikjsihhjjhfuu'>
>>> type(69696969969696875757676767576767676767676767676767675767676767676767)
<class 'int'>
>>> #You see that it is returning an object?
>>> re.search('[a-j]*', 'blkepppeoikjsihhjjhfuu')
<re.Match object; span=(0, 1), match='b'>
>>> re.search('[j-z]*', 'blkepppeoikjsihhjjhfuu')
<re.Match object; span=(0, 0), match=''>
>>> re.findall('[j-z]*', 'blkepppeoikjsihhjjhfuu')
['', 'lk', '', 'ppp', '', 'o', '', 'kjs', '', '', '', 'jj', '', '', 'uu', '']
>>> re.findall('[j-z]+', 'blkepppeoikjsihhjjhfuu')
['lk', 'ppp', 'o', 'kjs', 'jj', 'uu']
>>> type(type(int))
<class 'type'>
>>> type(re.findall('[j-z]+', 'blkepppeoikjsihhjjhfuu'))
<class 'list'>
>>> type(re.search('.*', 'blkepppeoikjsihhjjhfuu'))
<class 're.Match'>
>>> type(type(re.search('.*', 'blkepppeoikjsihhjjhfuu')))
<class 'type'>
>>> #What a weird object.
>>> re.match('^[0-9]{4}\s[0-9]{4}$',input('Phone number pls: ')) #??????????????????????????????????????
Phone number pls: 1234 5678
<re.Match object; span=(0, 9), match='1234 5678'>
>>> re.match('^[0-9]{4}\s[0-9]{4}$',input('Phone number pls: ')) #??????????????????????????????????????
Phone number pls: 6-7
>>> #does not return anything
>>> 
... Complete help docs: 864 lines, most is spent yapping about their classes.
... The most important parts are in a doc above.
... Do not run this file. It is a help file.
... '''

print('The docs are called classes_doc and patterns_doc')
