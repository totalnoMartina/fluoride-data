# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import lxml
from functions import spreadsheet, typing



def welcome_user():
    ask_usr = input('What is your name? \n')
    name = ask_usr
    msg = print(f'Welcome to Exploration of Data on Fluoride {name}')
    return msg




def main():
    """Function to run all functions """
    while True:
        welcome_user()
        break

main()
