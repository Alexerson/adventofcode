
def execute(memory):

    pointer = 0

    while (instruction:=memory[pointer]) != 99:
        
        if instruction == 1:
            address_first_param = memory[pointer + 1]
            address_second_param = memory[pointer + 2]
            address_third_param = memory[pointer + 3]
            memory[address_third_param] = memory[address_first_param] + memory[address_second_param]
            pointer += 4
            
        elif instruction == 2:
            address_first_param = memory[pointer + 1]
            address_second_param = memory[pointer + 2]
            address_third_param = memory[pointer + 3]
            memory[address_third_param] = memory[address_first_param] * memory[address_second_param]
            pointer += 4

        else:
            raise ValueError("This should not happen")

    return memory