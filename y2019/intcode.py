
def execute(memory, inputs=None):

    if inputs is None:
        inputs = []

    outputs = []

    pointer = 0

    while (opcode:=memory[pointer]) != 99:

        instruction = opcode % 100
        parameter_modes = opcode // 100

        if instruction == 1:
            params_count = 3
        elif instruction == 2:
            params_count = 3
        elif instruction == 3:
            params_count = 1
        elif instruction == 4:
            params_count = 1
        elif instruction == 5:
            params_count = 2
        elif instruction == 6:
            params_count = 2
        elif instruction == 7:
            params_count = 3
        elif instruction == 8:
            params_count = 3
            
        params = [
            (
                memory[pointer + 1 + index], 
                (parameter_modes // (10**index)) % 10**(index+1) 
            )
            for index in range(params_count)
        ]

        values = [param[0] if param[1] == 1 else memory[param[0]] for param in params]

        if instruction == 1:
            memory[params[2][0]] = values[0] + values[1]
            
        elif instruction == 2:
            memory[params[2][0]] = values[0] * values[1]

        elif instruction == 3:
            memory[params[0][0]] = inputs.pop()

        elif instruction == 4:
            outputs.append(values[0])

        elif instruction == 5:
            if values[0] != 0:
                pointer = values[1] - 1 - params_count

        elif instruction == 6:
            if values[0] == 0:
                pointer = values[1] - 1 - params_count

        elif instruction == 7:
            memory[params[2][0]] = int(values[0] < values[1])

        elif instruction == 8:
            memory[params[2][0]] = int(values[0] == values[1])

        else:
            raise ValueError("This should not happen")

        pointer += 1 + params_count

    return memory, outputs