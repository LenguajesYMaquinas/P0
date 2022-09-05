from tkinter import Variable


def file_reader(route: str)->list:

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

def verify_opened_closed_instructions(program: list)->bool:

    closed_instructions = {"PROG": False, "keys": {}}

    for i in program:
        if "PROG" in i:
            closed_instructions["PROG"] = True if closed_instructions["PROG"] == False else False

    print(closed_instructions["PROG"])

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
    if verify_opened_closed_instructions(program) and verificar_secuancia(program):
        print("correcto")
    else:
        print("incorrecto")