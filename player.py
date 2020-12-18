class Player:
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color
        self.captured_cells = 0

    def increment_captured_cells(self):
        self.captured_cells += 1

    def reset_captured_cells(self):
        self.captured_cells = 0

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'
