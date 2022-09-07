
"---------------------Declarations---------------------"

from ast import arguments
from distutils.log import FATAL
from multiprocessing import parent_process
from turtle import position


declared_variables = []

commands = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop"]

directions = ["north", "south", "east", "west", ""]

conditions = ["isfacing", "isValid", "canWalk", "not"]

"---------------------Auxiliar functions---------------------"

def clean_arguments(string:str)->list:

    first_parenthesis = 0
    second_parenthesis = 0
    position = 0

    for char in string:

        if char == "(":
            first_parenthesis = position
        if char == ")":
            second_parenthesis = position

        position += 1

    string = string[first_parenthesis + 1:second_parenthesis]
    arguments = string.split(",")

    return arguments
        

"---------------------File reader function---------------------"

def file_reader(route: str)->list:

    """
    
        Read the program in the txt file and savit in a list of lists, where each list is a line of the txt file. Also, delete the unnecesary spaces.

    """

    file = open(route,'r')
    line = file.readline()


    file_lines = []

    while line != "":
        file_lines.append(line.split())
        line = file.readline()

    for line in file_lines:
        for sstring in line:
            sstring.replace(" ", "")

    return file_lines

"---------------------Verifyer functions---------------------"

def verify_opened_closed_procedure(program:list)->bool:
    
    """

    Verify a procedure was closed and opened.

    """

    output = False
    states = {
            "PROC": 0,
            "CORP": 0, 
        }

    for i in program:
        if "PROC" in i:
            states["PROC"] = states["PROC"] + 1
        if "CORP" in i:
            states["CORP"] = states["CORP"] + 1

    if states["PROC"]==states["CORP"]:
        output = True

    return output

def verify_opened_closed_program(program:list)->bool:

    """

    Verify the program was closed and opened.

    """

    output = False
    states = {
            "PROG": 0,
            "GORP": 0, 
        }

    for i in program:
        if "PROG" in i:
            states["PROG"] = states["PROG"] + 1
        if "GORP" in i:
            states["GORP"] = states["GORP"] + 1

    if states["PROG"]==states["GORP"] and states["PROG"]!=0 and states["GORP"]!=0:
        output = True

    return output

    return output

def verifiy_var_declarations(program:list)->bool:

    """
    
    Verify the correct syntax in the variable declarations.

    """

    output = False
    var_counter = 1
    states = {}

    for i in program:
        if "var" in i:
            states["var_"+str(var_counter)] = False
            if len(i) > 1 and i[len(i)-1][len(i[len(i)-1])-1] == ";":
                states["var_"+str(var_counter)] = True
            var_counter += 1

    if False not in list(states.values()):
        output = True

    return output

def declare_variables(program: list):

    """

        Save the correct declared variables.

    """

    for i in program:
        if "var" in i and len(i) > 1 and i[len(i)-1][len(i[len(i)-1])-1] == ";":
            i.remove("var")
            for name in i:
                name = name.replace(",", "")
                name = name.replace(";", "")
                declared_variables.append(name)

def declare_parameters(program: list):

    """

        Save as variables the arguments in a procedure

    """

    for i in program:
        if "PROC" in i and len(i) > 1 and i[len(i)-1][len(i[len(i)-1])-1] == ";":
            i.remove("var")
            for name in i:
                name = name.replace(",", "")
                name = name.replace(";", "")
                declared_variables.append(name)

def verify_arguemts_in_commands(program:list)->bool:

    """
    
        Verify that the parameters inserted as arguments of a command are valid.

    """

    arguments = []

    for line in program:
        for string in line:
            for command in commands:
                if command in string:
                    arguments += clean_arguments(string)

    arguments_validations = {}

    for argument in arguments:
        arguments_validations[argument] = False
        if argument in declared_variables or argument in directions or argument in commands or argument.isdigit():
            arguments_validations[argument] = True

    output = True

    for i in list(arguments_validations.values()):
        if i == False:
            output = False  

    return output
                    
"---------------------Main function---------------------"

def verify_program(program)->bool:
    if verify_opened_closed_program(program) and verifiy_var_declarations(program) and verify_opened_closed_procedure(program) and verify_arguemts_in_commands(program):
        print("\nThe program is correct.\n")
    else:
        print("\nThe program is not correct.\n")
