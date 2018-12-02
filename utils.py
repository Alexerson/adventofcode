def data_import(filename, cast=str):
    data = []
    with open(filename) as file:
        line = file.readline()
        while line:
            if line.strip():
                data.append(cast(line.strip()))
            line = file.readline()
    return data
