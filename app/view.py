import model

file_route = "./data/"

def execute_appplication():

    route = input("Please, enter the name of the text file: ")
    file_route = file_route + route
    program = model.file_reader(file_route)
    model.verify_program(program)

execute_appplication()
