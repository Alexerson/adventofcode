
class Program(object):

    def __init__(self, memory):
        self.memory = list(memory)
        self.memory += [0] * 10000
        self.pointer = 0
        self.finished = False
        self.relative_base = 0

    def run_until_output(self, inputs=None):
        memory = self.memory
        if inputs is None:
            inputs = []

        while True:
            output = None

            opcode = memory[self.pointer]

            instruction = opcode % 100
            parameter_modes = opcode // 100

            if instruction in (3, 4, 9):
                params_count = 1
            elif instruction in (5, 6):
                params_count = 2
            elif instruction in (1, 2, 7, 8):
                params_count = 3
            elif instruction in (99,):
                params_count = 0
                
            params = [
                (
                    memory[self.pointer + 1 + i], 
                    (parameter_modes // (10**i)) % 10 
                )
                for i in range(params_count)
            ]

            values = []
            for param in params:
                if param[1] == 0:
                    values.append(memory[param[0]])
                elif param[1] == 1:
                    values.append(param[0])
                elif param[1] == 2:
                    values.append(memory[param[0] + self.relative_base])
                else:
                    raise ValueError('Wrong mode')

            if instruction == 1:
                index_ = params[2][0]
                if params[2][1] == 2:
                    index_ += self.relative_base
                memory[index_] = values[0] + values[1]
                
            elif instruction == 2:
                index_ = params[2][0]
                if params[2][1] == 2:
                    index_ += self.relative_base
                memory[index_] = values[0] * values[1]

            elif instruction == 3:
                index_ = params[0][0]
                if params[0][1] == 2:
                    index_ += self.relative_base
                memory[index_] = inputs.pop(0)

            elif instruction == 4:
                output = values[0]

            elif instruction == 5:
                if values[0] != 0:
                    self.pointer = values[1] - 1 - params_count

            elif instruction == 6:
                if values[0] == 0:
                    self.pointer = values[1] - 1 - params_count

            elif instruction == 7:
                index_ = params[2][0]
                if params[2][1] == 2:
                    index_ += self.relative_base
                memory[index_] = int(values[0] < values[1])

            elif instruction == 8:
                index_ = params[2][0]
                if params[2][1] == 2:
                    index_ += self.relative_base
                memory[index_] = int(values[0] == values[1])

            elif instruction == 9:
                self.relative_base += values[0]

            elif instruction == 99:
                self.finished = True
                return 

            else:
                raise ValueError("This should not happen")

            self.pointer += 1 + params_count

            if output is not None:
                return output
