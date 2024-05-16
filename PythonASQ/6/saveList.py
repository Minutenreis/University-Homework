def save_list(list: list, path: str):
    with open(path, "w") as f:
        for item in list:
            f.write(type(item).__name__+" ")
            f.write(str(item).replace("\n", "%0A").replace("\r", "%0D"))
            f.write("\n")

def load_list(path: str) -> list:
    result = []
    elements = open(path, 'r').readlines()
    for element in elements:
        type = element.split()[0]
        value = element[len(type)+1:].replace("\n","").replace("%0A", "\n").replace("%0D", "\r")
        if type == "str":
            result.append(value)
        elif type == "int":
            result.append(int(value))
        elif type == "float":
            result.append(float(value))
        elif type == "bool":
            result.append(value == str(True))
        elif type == "NoneType":
            result.append(None)
    return result

# Test the functions
list = ["str\n\t\r", 1, 1.0, True, False, None]
save_list(list, "Test.txt")
print(load_list("Test.txt"))