class Handheld:
    def __init__(self, program, index):
        self.program = program
        self.pointer = 0
        self.memory = []
        self.acc = 0
        self.replace_op(index)

    def run(self):
        while True:
            if self.pointer >= len(self.program):
                print(self.acc)
                return True
            elif self.pointer not in self.memory:
                self.memory.append(self.pointer)
            else:
                print(f"Loop detected after line {self.memory[-1]}")
                return False
            self.execute(self.program[self.pointer])
    
    def execute(self, instruction):
        instruction, value = instruction.split()
        match instruction:
            case "nop":
                self.pointer += 1
                return
            case "jmp":
                self.pointer += int(value)
                return
            case "acc":
                self.acc += int(value)
                self.pointer += 1
                return

    def replace_op(self, index):
        bad_op = self.program[index]
        if bad_op[:3] == "jmp":
            bad_op = "nop" + bad_op[3:]
        elif bad_op[:3] == "nop":
            bad_op = "jmp" + bad_op[3:]
        print(f"replacing {self.program[index]} with instruction {bad_op}")
        self.program[index] = bad_op

with open("input.txt") as file:
    program = file.read().split("\n")

completed = False
i = 0
while not completed:
    print(f"Starting Console {i}")
    console = Handheld(program[:], i)
    completed = console.run()
    i += 1
