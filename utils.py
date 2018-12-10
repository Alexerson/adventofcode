def data_import(filename, cast=str, split_line=False):
    data = []
    with open(filename) as file:
        line = file.readline()
        while line:
            if line.strip():

                if split_line:
                    line = line.split()
                    data.append([cast(item.strip()) for item in line])
                else:
                    data.append(cast(line.strip()))

            line = file.readline()
    return data
