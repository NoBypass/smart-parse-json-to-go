import json


def main():
    json_input = input("Enter JSON file location: ")

    with open(json_input, "r") as f:
        json_input = f.read()

    json_input = json.loads(json_input)

    name = input("Enter struct name: ")

    with open(name + ".go", "w") as f:
        f.write("package main\n\n")
        f.write("type " + name + new_struct(json_input))

def new_struct(go_struct: dict):
    out = "struct {\n"
    for key, value in go_struct.items():
        out += title(key) + " " + get_type(value) + " `json:\"" + key + "\"`\n"
    return out + "}"

def new_slice(go_slice: list):
    if len(go_slice) == 0:
        return " []interface{}"
    return " []" + get_type(go_slice[0])

def get_type(value: str|dict|list):
    t = type(value)
    final = ""

    if t is dict:
        final = new_struct(value)
    elif t is list:
        final = new_slice(value)
    elif t is str:
        final = "string"
    elif t is bool:
        final = "bool"
    elif t is int:
        final = "int"
    elif t is float:
        final = "float64"
    else:
        final = "interface{}"
    return final

def title(s: str):
    split = multi_split(s, ["_", "-"])
    final = ""
    for s in split:
        if len(s) < 1:
            continue
        final += s[0].upper() + s[1:]
    return final

def multi_split(s: str, delimiters: list):
    out = [s]
    for delimiter in delimiters:
        temp = []
        for item in out:
            temp += item.split(delimiter)
        out = temp
    return out

if __name__ == '__main__':
    main()
