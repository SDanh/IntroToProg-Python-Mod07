# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: An example of Python Pickling/Binary Files & Exception Handling
# ChangeLog (Who,When,What):
# SDanh, 8.22.2020, Created Script, basic implementation of Pickling/Unpickling
# SDanh, 8.23.2020, Added exception handling, implemented UI/Menu
# SDanh, 8.24.2020, Review & Commenting of Code
# ---------------------------------------------------------------------------- #

# Research Sources:
# https://www.programiz.com/python-programming/exception-handling
# https://www.tutorialspoint.com/python-pickling
# http://cs.carleton.edu/cs_comps/1213/pylearn/final_results/encyclopedia/
# https://docs.python.org/3/library/pickle.html

import pickle

# DATA----------
file_name = "data.txt"
strMenu = "1 - Print | 2 - Load | 3 - Save | 4 - Add | 5 - Quit | 6 - Help"
lstData = []
strHelp = """
This is an example of Pickling/Unpickling Binary Files & Exception Handling:
______________
data.txt - 'default' data file for loading & saving. Will load as normal.

empty.txt - intentionally empty file. loading this file will cause an End of File Error

image.png - png file. loading this file will cause an Unpickling Error

any other file name - file does not exist and will lead to File Not Found Error
"""

# PROCESSING----------
class Binary_File:

    # helper function to ask for filename
    def file_picker(self):
        file_name = input("Pick File (Default is data.txt): ")
        return file_name

    # loads a binary file containing a list
    def load_file (file_name, lstData):
        lstData.clear()
        try:
            fileData = open(file_name, "rb")
            lstData = pickle.load(fileData)
            fileData.close()
        except FileNotFoundError as e:
            print(e.__str__())
            print(file_name + " doesn't exist!")
        except EOFError as e:
            print(e.__str__())
            print("Reached End of File!")
        except pickle.UnpicklingError as e:
            print(e.__str__())
            print(file_name + " Cannot be Read!")
        except BaseException:
            print("Unknown Error!")

        return lstData

    # writes to the binary file a list
    def write_file (file_name, lstData):
        fileData = open(file_name, "wb")
        pickle.dump(lstData,fileData)
        fileData.close()
        return lstData

BF = Binary_File()

# INTERFACE----------
while True:
    print(strMenu)
    strInput = input("input: ")
    strInput = strInput.lower()

    if strInput == '1':
        print(lstData)
        pass

    elif strInput == '2':
        print("Loading...")
        file_name = BF.file_picker()
        lstData = Binary_File.load_file(file_name, lstData)
        pass

    elif strInput == '3':
        print("Saving...")
        file_name = BF.file_picker()
        Binary_File.write_file(file_name, lstData)
        pass

    elif strInput == '4':
        print("Adding...")
        x = input("New Item: ")
        lstData.append(x)
        pass

    elif strInput == '5':
        break

    elif strInput == '6':
        print(strHelp)
        pass

    else:
        print("Wrong Input")
