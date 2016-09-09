#!/usr/bin/python
'''
Author: FATGEEK
Contact: fatgeek@gmail.com
Description: Little module helping me to import fonctions to the main project
Version: 0.1
'''
import os

class colors:
    DEFAULT = '\033[0m'
    BLACK = '\033[0;30m'
    BLUE = '\033[0;34m'
    GREEN = '\033[0;32m'
    CYAN = '\033[0;36m'
    RED = '\033[0;31m'
    PURPLE = '\033[0;35m'
    BROWN = '\033[0;33m'
    LGRAY = '\033[0;37m'
    DGRAY = '\033[1;30m'
    LBLUE = '\033[1;34m'
    LGREEN = '\033[1;32m'
    LCYAN = '\033[1;36m'
    LRED = '\033[1;31m'
    LPURPLE = '\033[1;35m'
    YELLOW = '\033[1;33m'
    WHITE = '\033[1;37m'

def WelcomeHeader():
    #Printing the Welcome Message
    os.system('clear')
    print(colors.LGREEN + "\n               ********************************************\n" + colors.DEFAULT)

    print(colors.LCYAN +"                      Welcome to EasyRogue.py v0.1 !!    " + colors.DEFAULT)
    print("\n                   Aircrack-suite, hostapd and dnsmasq   " + "\n                       are " + colors.LRED + "required " + colors.DEFAULT + "to proceed.")
    print(colors.LGREEN + "\n               ********************************************\n" + colors.DEFAULT)

def VariableColoring(Color, Variable):
    if Color == "C":
        Var = colors.LCYAN + Variable + colors.DEFAULT
    elif Color == "G":
        Var = colors.LGREEN + Variable + colors.DEFAULT
    elif Color == "R":
        Var = colors.LRED + Variable + colors.DEFAULT
    else:
        return Variable
    
    return Var

