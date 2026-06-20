#imports
import time
from tools import Tools
from technical import Technical
from docs import docs
from randoms import Randoms
from module_checker import IsModulePreset
#from games import Games
#from animations import Animations

class PythonShop:
    GUIDE = '''
        Okay, you asked for a long, long yapping.
        ...
        Input the name of the aisle, then the name of the product.

        AISLE 1: Math Tools (mathtools)
        - findounces: From kilograms and grams to stones, pounds, and ounces.
        - sum: Sums up integers and floats seperately, and prints the result. Good when you have 2 types of data and you need to seive and sum them up.
        - grades: Uses an, ahem, predetermined system to decide if you fail your Asian Parents or get to go to uni.
        - comma: Sticks commas into unbroken integers.
        - triangle: Prints a right-aligned triangle of odd numbers.'''
    def __init__(self):
        print("Welcome to PythonShop! \n We're a 'zha huo dian' which 'sells' tools, toys, and time wasters! ._. \n by :/, the annoying inline suggestions, and chatgpt")
        #smart ahh chinese (undetected) (inaccurate)

        self.tools = Tools()
        self.technical = Technical()
        self.docs = docs
        self.randoms = Randoms()
        self.module_checker = IsModulePreset()
        #self.games = Games()
        #self.animations = Animations()
        
        self.loop()

    def loop(self):
        print("Input 'guide' for the guide and 'exit' to ding-a-ling and leave the shop")
        self._input = input('._.> ')

        if self._input == "exit":
            pass
        elif self._input == "guide":
            for line in self.GUIDE.splitlines():
                print(line)
                time.sleep(0.2)

shop = PythonShop()#                                                  >.<
print("Goodbye -_-")#                                                                     >.<
#                                                                                                  >.<