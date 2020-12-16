class Player:
    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
