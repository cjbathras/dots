from singleton import Singleton


class Config(metaclass=Singleton):
    def __init__(self, rows=5, columns=5, cell_size=75, dot_radius=5):
        self._rows = rows
        self._columns = columns
        self._cell_size = cell_size
        self._dot_radius = dot_radius

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @property
    def cell_size(self):
        return self._cell_size

    @property
    def dot_radius(self):
        return self._dot_radius
