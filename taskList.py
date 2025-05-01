import json
from datetime import date

donnees = {}
with open("donnees.json", "r") as json_file : 
    donnees = json.load(json_file)

def max_keys(dictionnary):
    max_keys = 0
    if dictionnary == {}:
        return 0
    else:
        for keys in dictionnary.keys():
            if max_keys < int(keys):
                max_keys = int(keys)
        return max_keys

def command_in_user_input(user_input, command_list):
    for elt in command_list:
        if elt in user_input.split():
            user_command = elt
            break
    return user_command
    
def print_task(elt, donnees):
    print("id task : " + str(elt))
    print("description task : " + str(donnees[elt]["description"]))
    print("status : " + str(donnees[elt]["status"]))
    print("created At : " + str(donnees[elt]["createdAt"]))
    print("updated At : " + str(donnees[elt]["updatedAt"]))
    print("----------------------------------------------------------")
    
def add_task(command, user_input, donnees):
    add_task = user_input.split()
    add_task_copy = add_task[:]
    add_task_copy.remove(command)
    description_task = ' '.join(add_task_copy)
    donnees[max_keys(donnees)+1] = {"description" : description_task, "status": "todo", "createdAt":date.today().isoformat(), "updatedAt": date.today().isoformat()}
    with open("donnees.json", "w") as json_file :
        json.dump(donnees,json_file,indent=3)
        print("task has been added succesfully.")
    
def delete_task(command, user_input, donnees):
    input_split = user_input.split()
    input_copy = input_split[:]
    del(input_copy[0])
    id_task = int(input_copy[0])
    if str(id_task) in donnees:
        del(donnees[str(id_task)])
        with open("donnees.json", "w") as json_file : 
            json.dump(donnees,json_file, indent=3) 
        print("task has been deleted successfully")
    else : 
        print("this task is not in the file")

def list_all_task(donnees):
    for elt in donnees:
        print("value of the key")
        print_task(elt, donnees)
        
def list_todo_task(donnees):
    for elt in donnees:
        if donnees[elt]["status"] == "todo":
            print("valeur de la clé : " + str(elt))
            print_task(elt, donnees)

def list_done_task(donnees):
    for elt in donnees:
        if donnees[elt]["status"] == "done":
            print_task(elt, donnees)

def list_in_progress_task(donnees):
    for elt in donnees.keys():
        if donnees[elt]["status"] == "in progress":
            print_task(elt, donnees)

def mark_task(user_input, status,command):
    input_split = user_input.split()
    input_copy = input_split[:]
    input_copy.remove(command)
    id_task = str(input_copy[0])
    donnees[id_task]["status"] = status
    with open("donnees.json", "w") as json_file:
        json.dump(donnees,json_file, indent = 3)
        print("task status has been modified succesfully.")

def update_task(user_input,donnees, command):
    input_split = user_input.split()
    input_copy = input_split[:]
    print("copie de l\'entree utilisateur : ")
    print(input_copy)
    input_copy.remove(command)
    print("remove update : ")
    print(input_copy)
    #print(input_l)
    id_task = str(input_copy[0])
    if(id_task == ''):
        print("You forgot to enter the id task before updating the name task")
    else:
        description = input_copy[1]
        donnees[id_task]["description"] = description
        donnees[id_task]["updatedAt"] = date.today().isoformat()
    with open("donnees.json", "w") as json_file :
        json.dump(donnees,json_file, indent = 3)
        print("task has been updated succesfully")
command_list = ["add", "update", "delete", "list_todo", "mark-in-progress", "mark-done", "list_done", "list", "list in progress"]
user_input = input("please, enter a commande in the interface : ")
command = command_in_user_input(user_input, command_list)
if(command == "add"):
    description = add_task("add", user_input,donnees)
elif(command == "delete"):
    delete_task("delete", user_input, donnees)
elif(command == "list"):
    list_all_task(donnees)
elif(command == "list_todo"):
    #print("hello world ! ")
    list_todo_task(donnees)
elif(command == "list_done"):
    list_done_task(donnees)
elif(command == "mark-in-progress"):
    mark_task(user_input, "in-progress","mark-in-progress")
elif(command == "mark-done"):
    mark_task(user_input, "done","mark-done")
elif(command == "update"):
    update_task(user_input,donnees, "update")
else : 
    print("no command find with this syntax")
    
