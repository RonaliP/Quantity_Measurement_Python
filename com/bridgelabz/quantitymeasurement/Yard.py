class Yard:

    def __init__(self, yard):
        self.yard = yard

    def __eq__(self, other):
        if isinstance(other, Yard):
            if self.yard == other.yard:
                return True
        return False