# import relevant modules  - see which exactly you need
# import lxml - for text extraction
# from functions import spreadsheet, typing - for presenting text to user

def welcome_user():
    """ Welcome message to users and itroduction to fluoride """
    ask_usr = input('What is your name? \n')
    name = ask_usr
    msg = print(f'Welcome to Exploration of Data on Fluoride {name}')
    return msg


def get_text():
    """ Get text to be presented to user """
    pass


def get_excel():
    """ Get sheets from excel documents """
    pass


def get_columns():
    """ Get specific information from certain columns or tables """
    pass


def generate_chart():
    """ Generate a chart for user to get a visual image - pandas? """
    pass


class Chart:
    """ Create in instance to generate chart for user """

def main():
    """Function to run all functions """
    while True:
        welcome_user()
        break


main()
