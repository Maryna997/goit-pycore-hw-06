class Field:
    # Базовий клас для полів запису

    def __init__(self, value):
        # Ініціалізувати поле введенням значення
        self.value = value

    def __str__(self):
        # Повернути рядкове відображення значення
        return str(self.value)