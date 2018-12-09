class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return str(self.__dict__)
    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise NotImplementedException()

    def __mul__(self, other):
        if isinstance(other, float):
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            raise NotImplementedException()
