

class Program(object):

    def __init__(self, memory):
        self.memory = list(memory)
        self.pointer = 0
        self.finished = False

    def execute(self, inputs=None):

        memory = self.memory
        if inputs is None:
            inputs = []

        outputs = []

        while (opcode:=memory[self.pointer]) != 99:

            instruction = opcode % 100
            parameter_modes = opcode // 100

            if instruction in (1, 2, 7, 8):
                params_count = 3
            elif instruction in (3, 4):
                params_count = 1
            elif instruction in (5, 6):
                params_count = 2
                
            params = [
                (
                    memory[self.pointer + 1 + index], 
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
                memory[params[0][0]] = inputs.pop(0)

            elif instruction == 4:
                yield values[0]

            elif instruction == 5:
                if values[0] != 0:
                    self.pointer = values[1] - 1 - params_count

            elif instruction == 6:
                if values[0] == 0:
                    self.pointer = values[1] - 1 - params_count

            elif instruction == 7:
                memory[params[2][0]] = int(values[0] < values[1])

            elif instruction == 8:
                memory[params[2][0]] = int(values[0] == values[1])

            else:
                raise ValueError("This should not happen")

            self.pointer += 1 + params_count

        self.finished = True
