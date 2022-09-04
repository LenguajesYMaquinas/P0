import model

file_route = "./data/example_1.txt"

def execute_appplication():

    route = input("Please, enter the route of the text file: ")
    program = model.file_reader(file_route)
    model.verify_program(program)

execute_appplication()