def data_import(filename, cast=str, split_char=None, rstrip=False):
    data = []
    with open(filename) as file:
        line = file.readline()
        while line:
            if rstrip and line.rstrip() or line.strip():

                if split_char is not None:
                    line = line.split(split_char)
                    data.append([cast(item.strip()) for item in line])
                else:
                    data.append(cast(rstrip and line.rstrip() or line.strip()))

            line = file.readline()
    return data
