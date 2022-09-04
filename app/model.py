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

def verify_opened_closed_program(program:list)->bool:

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

            

def verify_program(program)->bool:
    if verify_opened_closed_program(program) and verifiy_var_declarations(program):
        print("\nThe program is correct.\n")
    else:
        print("\nThe program is not correct.\n")