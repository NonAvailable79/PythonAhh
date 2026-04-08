Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
help
Type help() for interactive help, or help(object) for help about object.
199
199
{1]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
{1}
{1}
777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777 ** -1
1.2857142857142857e-102
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells)
    
SyntaxError: expected ':'
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if cells > 0:
            return 'Yes, living'
    def grow(self, years)
    
SyntaxError: expected ':'
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if cells > 0:
            return 'Yes, living'
    def grow(self, years):
        yet = self.cellnum
        for i in years:
            yet = yet * 1.4
        return round(yet)

    
amoeba = Organism('bacteria', 1)
amoeba.living()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    amoeba.living()
  File "<pyshell#20>", line 8, in living
    if cells > 0:
NameError: name 'cells' is not defined
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if self.cellnum > 0:
            return 'Yes, living'
    def grow(self, years):
        yet = self.cellnum
        for i in years:
            yet = yet * 1.4
        return round(yet)

    
amoeba.living()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    amoeba.living()
  File "<pyshell#20>", line 8, in living
    if cells > 0:
NameError: name 'cells' is not defined
amoeba = Organism('bacteria', 1)
amoeba.living()
'Yes, living'
amoeba.grow(67)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    amoeba.grow(67)
  File "<pyshell#24>", line 12, in grow
    for i in years:
TypeError: 'int' object is not iterable
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if self.cellnum > 0:
            return 'Yes, living'
    def grow(self, years):
        yet = self.cellnum
        for i in range(years):
            if yet == 1:
                yet = 1
            else:
                yet = yet * 1.4
        return round(yet)

    
amoeba = Organism('bacteria', 1)
amoeba.living()
'Yes, living'
chair = Organism('Singapore', 0)
chair.living()]
SyntaxError: unmatched ']'
chair.living()
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if self.cellnum > 0:
            return 'Yes, living'
        else:
            return 'No'
        
    def grow(self, years):
        yet = self.cellnum
        for i in range(years):
            if yet == 1:
                yet = 1
            else:
                yet = yet * 1.4
        return round(yet)

    
amoeba = Organism('bacteria', 1)
chair = Organism('Singapore', 0)
chair.living()
'No'
amoeba.grow(95672048576)

========================================================================== RESTART: Shell =========================================================================
amoeba
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    amoeba
NameError: name 'amoeba' is not defined
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if self.cellnum > 0:
            return 'Yes, living'
        else:
            return 'No'

    def grow(self, years):
        yet = self.cellnum
        for i in range(years):
            if yet == 1:
                yet = 1
            else:
                yet = yet * 1.4
        return round(yet)

    
amoeba = Organism('bacteria', 1)
amoeba.grow(956)
1
human = Organism ('animal', 1440000)
human
<__main__.Organism object at 0x0000025F4668FD90>
type(human)
<class '__main__.Organism'>
type(3)
<class 'int'>
human.grow(12)
81639234

======================================== RESTART: C:\Users\USER\Desktop\py collection\anything\Complete exam collection.py ========================================
This is bro's random exam
10 in 1 program!!!!!!!!!!! 


Which question do you want to find out? -1 to kill, range is 1 to 10
: 
Traceback (most recent call last):
  File "C:\Users\USER\Desktop\py collection\anything\Complete exam collection.py", line 14, in <module>
    question = int(input('\nWhich question do you want to find out? -1 to kill, range is 1 to 10\n: '))
ValueError: invalid literal for int() with base 10: ''
help(print)
Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.

    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.


======================================== RESTART: C:\Users\USER\Desktop\py collection\anything\Complete exam collection.py ========================================
This is bro's random exam
10 in 1 program!!!!!!!!!!! 


Which question do you want to find out? -1 to kill, range is 1 to 10
: 
Traceback (most recent call last):
  File "C:\Users\USER\Desktop\py collection\anything\Complete exam collection.py", line 14, in <module>
    question = int(input('\nWhich question do you want to find out? -1 to kill, range is 1 to 10\n: '))
KeyboardInterrupt
amoeba
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    amoeba
NameError: name 'amoeba' is not defined
class Organism:
    '''
Do you live?'''
    def __init__(self, kingdom, cells):
        self.kingdom = kingdom
        self.cellnum = cells
    def living(self):
        if self.cellnum > 0:
            return 'Yes, living'
    def grow(self, years):
        yet = self.cellnum
        for i in range(years):
            if yet == 1:
                yet = 1
            else:
                yet = yet * 1.4
        return round(yet)

    
class Animal(Organism):
    def __init__ (self, name, species, speech):
        self.name = name
...         self.type = species
...         self.talk = speech
...     def communicate(self):
...         return self.talk
...     def populate(self, place, num):
...         population = 2
...         for i in range(num):
...             population *= 2
...         return 'You have succesfully populated ' + place  + ' for ' + num + ' years, resulting in a population of ' + population
... 
...     
>>> me = Animal('me', human, 'Hi!')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    me = Animal('me', human, 'Hi!')
NameError: name 'human' is not defined
>>> me = Animal('me', 'human', 'Hi!')
>>> me.communicate
<bound method Animal.communicate of <__main__.Animal object at 0x0000024E0D002A50>>
>>> me.communiacte()
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    me.communiacte()
AttributeError: 'Animal' object has no attribute 'communiacte'. Did you mean: 'communicate'?
>>> me.communicate()
'Hi!'
>>> me.populate('city')
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    me.populate('city')
TypeError: Animal.populate() missing 1 required positional argument: 'num'
>>> me.populate('city', 400)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    me.populate('city', 400)
  File "<pyshell#65>", line 12, in populate
    return 'You have succesfully populated ' + place  + ' for ' + num + ' years, resulting in a population of ' + population
TypeError: can only concatenate str (not "int") to str
>>> #Honestly, I give up here.
>>> #EVEN IF YOU KNOW HOW, THERE ARE ALWAYS SYNTAX RULES TO OBEY.
>>> KeyboardInterrupt
