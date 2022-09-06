
"---------------------Declarations---------------------"

declared_variables = []

instructions = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop", "walk", "isfacing", "isValid", "canWalk", "not"]

"---------------------Auxiliar functions---------------------"

def confirmar_PC(parte, pos):

    for o in range(pos, len(parte)):
        Lugar = parte[o] 
        LugarI = len(Lugar)
        todoBien= " "
        if LugarI == 1 or LugarI == 2:
            comprobar= Lugar[-1]
        else:
            todoBien= False
            break

        if comprobar == "fi" or comprobar == "od" or comprobar == "per" or comprobar == "{":
            todoBien= True
        elif comprobar == "}":
            todoBien= True
            break
        else:
            sig= parte[o+1]
            if sig == "}":
                todoBien= True

        return todoBien

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

def verify_arguemts(program:list)->bool:

    """
    
        Verify that the parameters inserted as arguments of a command are valid.

    """

    for line in program:
        for string in program:
            if "walk" in string:
                return True

"---------------------Main function---------------------"

def verify_program(program)->bool:
    if verify_opened_closed_program(program) and verifiy_var_declarations(program) and verify_opened_closed_procedure(program):
        print("\nThe program is correct.\n")
    else:
        print("\nThe program is not correct.\n")
