import queue

class Process:
    def __init__(self, pid, instructions):
        self.pid = pid
        self.state = 'pronto'
        self.pc = 0
        self.registers = {}
        self.memory = []
        self.instructions = instructions
        self.tasks = []

class ProcessManager:
    def __init__(self):
        self.process_list = []
        self.pid_counter = 0

    def create_process(self, instructions):
        pid = self.pid_counter
        self.pid_counter += 1
        process = Process(pid, instructions)
        self.process_list.append(process)
        return process

    def terminate_process(self, pid):
        self.process_list = [p for p in self.process_list if p.pid != pid]

    def get_process(self, pid):
        for process in self.process_list:
            if process.pid == pid:
                return process
        return None

    def update_process_state(self, pid, new_state):
        process = self.get_process(pid)
        if process:
            process.state = new_state

class ProcessScheduler:
    def __init__(self):
        self.ready_queue = queue.Queue()

    def add_process(self, process):
        self.ready_queue.put(process)

    def schedule(self):
        if not self.ready_queue.empty():
            process = self.ready_queue.get()
            return process
        return None

class VirtualMachine:
    def __init__(self, process_manager, process_scheduler):
        self.process_manager = process_manager
        self.process_scheduler = process_scheduler

    def execute(self):
        while True:
            process = self.process_scheduler.schedule()
            if process:
                self.execute_process(process)

    def execute_process(self, process):
        process.state = 'executando'
        while process.pc < len(process.instructions):
            instruction = process.instructions[process.pc]
            self.execute_instruction(process, instruction)
            process.pc += 1
        process.state = 'terminado'

    def execute_instruction(self, process, instruction):
        if instruction == "MOVE":
            print(f"Process {process.pid}: Moving robot")
        elif instruction == "PICK":
            print(f"Process {process.pid}: Picking up object")
        elif instruction == "DROP":
            print(f"Process {process.pid}: Dropping object")
        elif instruction == "SENSE":
            print(f"Process {process.pid}: Sensing environment")
        # Adicione outras instruções conforme necessário

# Exemplo de uso

# Criar gerenciador e escalonador de processos
process_manager = ProcessManager()
process_scheduler = ProcessScheduler()

# Criar alguns processos com instruções simples
process1 = process_manager.create_process(["MOVE", "PICK", "MOVE", "DROP"])
process2 = process_manager.create_process(["SENSE", "MOVE", "PICK", "SENSE"])

# Adicionar processos ao escalonador
process_scheduler.add_process(process1)
process_scheduler.add_process(process2)

# Criar e executar a VM
vm = VirtualMachine(process_manager, process_scheduler)
vm.execute()
