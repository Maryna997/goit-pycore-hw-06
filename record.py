from phone import Phone
from name import Name


class Record:
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.

    def __init__(self, name):
        # Ініціалізувати Record з іменем і порожнім списком телефонів
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def __str__(self):
        # реалізація класу у вигляді рядка
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def add_phone(self, number: str):
        # функція для додавання номера телефону
        self.phones.append(Phone(number))

    def remove_phone(self, number: str):
        # функція для видалення номера телефону
        self.phones = list(filter(lambda phone: phone == number, self.phones))

    def edit_phone(self, old_number, new_number):
        # функція для редагування номера телефону
        self.phones = list(map(
            lambda phone: Phone(new_number) if phone.value == old_number else phone, self.phones,
        ))

    def find_phone(self, number):
        # функція для знаходження номера телефону
        for phone in self.phones:
            if phone.value == number:
                return phone
