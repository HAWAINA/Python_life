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
        return f'Результат суммы: {self.__cpu + self.__memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __str__(self):
        return f'Центральный процессор компьютера: {self.cpu}\nПамять компьютера: {self.memory}\n'

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def __str__(self):
        return f'список сим-карт: {list}'

    def call(self, sim_card_number, call_to_number):
        return f'Звонок на номер: {call_to_number} от сим: {sim_card_number}'

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_card_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_card_list)

    def GPS(self, location):
        print(f'Двигайтесь вперед, чтобы получить: {location}')

    def __str__(self):
        return f'Центральный процессор телефона: {self.cpu}\nПамять телефона: {self.memory}\n'


computer = Computer(64, 512)
print(computer.make_computations())
sim_1 = 'MegaCome'
sim_2 = 'Oshka'
list = [sim_1, sim_2]
phone = Phone(1)


print(phone.call(list[0], 996552541188))
smartphone = SmartPhone(8, 128, list)
smartphone.GPS('Сумму')


print(computer)
print(phone)
print(smartphone)
print(computer > smartphone)

