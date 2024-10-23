from field import Field

class Name(Field):
    # Являє собою поле для зберігання імені

    def __init__(self, name):
        self.value = name