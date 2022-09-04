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

def verify_program(program)->bool:
    if verify_opened_closed_instructions:
        print(True)