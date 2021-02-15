def load_input(_path : str):
    with open(_path) as json_file:
        data = json.load(json_file)
    return data

def get_number_images(_path : str):
    cwd = os.getcwd() + '\\' + _path
    entries = listdir(cwd)
    return entries - 1

def load_input(_path : str):
    with open(_path) as json_file:
        data = json.load(json_file)
    return data