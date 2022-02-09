class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f'Result of sum: {self.__cpu + self.__memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def info(self):
        return f'CPU of computer {self.cpu}\nMemory of computer {self.memory}\n'
    def __str__(self):
        return f'CPU of computer{self.cpu} \nMemory of computer{self.memory}\n'

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def sims(self):
        return f'list of sim card: {list}'

    def __str__(self):
        return f'list of sim card: {list}'

    def call(self, sim_card_number, call_to_number):
        return f'Calling to number{call_to_number} from sim{sim_card_number}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def use_gps(self, location):
        print(f'Move forward to get:{location}')

    def __str__(self):
        return f'CPU of phone{self.cpu}\nMemory of phone{self.memory}\n'


computer = Computer(6, 1024)
print(computer.info())
print(computer.make_computations())
sim_1 = '1 - MegaCome'
sim_2 = '2 - Beeline'
list = [sim_1, sim_2]
phone = Phone(1)
phone.sims()

print(phone.call(list[0], 755670170))
smartphone = SmartPhone(3, 12, list)
smartphone.use_gps('Sum')
smartphone.info()

print('_______________Results of str______________')
print(computer)
print(phone)
print(smartphone)
print(computer > smartphone)

