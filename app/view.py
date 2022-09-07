import model

def execute_appplication():

    file_route = "./data/"
    route = input("Please, enter the name of the text file: ")
    file_route = file_route + route
    program = model.file_reader(file_route)
    model.verify_program(program)
    print(model.verify_arguemts_in_commands(program))

execute_appplication()
