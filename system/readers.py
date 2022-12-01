class CommaReader:
    def __init__(self, file):
        self.file = file

    def read(self):
        return self.file.read().split(",")

class LineReader:
    def __init__(self, file):
        self.file = file

    def read(self):
        return self.file.read().splitlines()
    
class GridReader(LineReader):
    def __init__(self, file):
        super().__init__(file)

    def read(self):
        grid = super().read()
        
        for i in range(len(grid)):
            grid[i] = list(grid[i])

        return grid
    
class ReaderFactory:
    @classmethod
    def create(cls, type, file):
        if type == "comma":
            return CommaReader(file)
        elif type == "grid":
            return GridReader(file)
        else:
            return LineReader(file)
