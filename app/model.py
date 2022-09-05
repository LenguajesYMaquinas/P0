
"---------------------Declarations---------------------"

declared_variables = []

instructions = ["walk", "jump", "jumpTo", "veer", "look", "drop", "grab", "get", "free", "pop", "walk", "isfacing", "isValid", "canWalk", "not"]

"---------------------Auxiliar functions---------------------"

def number_of_arguments():
    return True

"---------------------Main functions---------------------"

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

def verify_opened_closed_program(program:list)->bool:

    """

    Verify the program was closed and opened.

    """

    output = False
    states = {
            "PROG": False,
            "GORP": False, 
        }

    for i in program:
        if "PROG" in i:
            states["PROG"] = True if states["PROG"] == False else False
        if "GORP" in i:
            states["GORP"] = True if states["GORP"] == False else False

    if states["PROG"]==True and states["GORP"]==True:
        output = True

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

def verify_declared_variables(program:list)->bool:

    """
    
        Verify that the variables inserted in the argument of a command were declared

    """

    states = {}

    for line in program:
        for string in program:
            if "walk" in string:
        
"---------------------Main function---------------------"

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


def verificar_secuancia(program):

    conclusion= " "
    posicion= 0
    for i in program:
        
        cerrar_P= 0

        if i == "{":
            cerrar_P+= 1
            a = confirmar_PC(program, posicion)

            if a == False:
                conclusion= False

        posicion+= 1

    return conclusion 

def verificar_Proc(program):
    conclusion= " "
    if program[0] == "PROG":
        program.pop(0)
    else:
        conclusion= False
        return conclusion
    
    if program[-1] == "CORP":
        program.pop(-1)
    else:
        conclusion= False
        return conclusion

    for i in program:
        control= 0
        if program[i] == "PROG":
            control+= 1

        if program[i] == "CORP":
            control-= 1

    if control != 0:
        conclusion= False
        return conclusion 
    else:
        conclusion= True

    return conclusion


def verify_program(program)->bool:
    if verify_opened_closed_program(program) and verifiy_var_declarations(program) and verificar_secuancia(program):
        print("\nThe program is correct.\n")
    else:
        print("\nThe program is not correct.\n")