# helpers
from datetime import datetime
import requests
import sys
import os

#  function to draw a header with text
def header():
    clear()
    draw('*')
    print("Images Analyzer".center(terminal_width()))
    draw('*')


#  function to get user input from a list of options
def get_user_input(options):
    for option in range(len(options)):
        print (options[option])
    return int(input('>>> '))

#  function to get file of any type from local directory and store them in a list
def get_local_file_list(directory,ftype):
    path = os.getcwd()+'/'+ directory
#    print (path)
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if ftype in file:
                files.append(os.path.join(r, file))

    return files





# function that returns terminal width size
def terminal_width():
    columns = os.get_terminal_size().columns
#    print(type(columns))
    return columns


# function to print a Time Stamp
def timestamp():
    print(str(datetime.now()))


# function to draw any character or symbol for the lenght of the terminal
def draw(symbol):
    try:
        maxcol = os.get_terminal_size().columns
    # piped output to file or other process
    except OSError:
        maxcol = sys.maxsize

    # check to be exactly one character or symbol
    if (len(symbol)>1):
        symbol = symbol[0]

    # print the symbol
    print(symbol*maxcol)


#  clear terminal screen function
def clear():
    os.system('clear')
#  TODO make it portable on windows



# Test zone


#print(get_local_file_list('images','.png'))

