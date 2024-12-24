class User:
    def __init__(self, first_name, last_name):
        # Конструктор, который принимает имя и фамилию
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        # Метод для печати имени
        print(self.first_name)

    def print_last_name(self):
        # Метод для печати фамилии
        print(self.last_name)

    def print_full_name(self):
        # Метод для печати полного имени (имя и фамилия)
        print(f"{self.first_name} {self.last_name}")

    