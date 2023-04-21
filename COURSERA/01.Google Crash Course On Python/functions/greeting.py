def greeting(name):
    print("Welcome, " + name)
    return None


def greeting_all(names):
    for i in names:
        greeting(i)


# list() is constructor of built-in class list
list_of_names = list()
list_of_names.append("Katty")
list_of_names.append("John")
list_of_names.append("Bob")


greeting_all(list_of_names)
