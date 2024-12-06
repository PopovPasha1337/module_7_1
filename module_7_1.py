class Figure:
    sides_count = 0

    def init(self, color, *sides):
        self._sides = list(sides) if len(sides) == self.sides_count else [1] * self.sides_count
        self.color = self.is_valid_color(color)
        self.filled = True

    def __is_valid_color(self, rgb):
        r, g, b = rgb
        if all(0 <= c <= 255 and isinstance(c, int) for c in (r, g, b)):
            return rgb
        return (0, 0, 0)

    def set_color(self, r, g, b):
        if self.__is_valid_color((r, g, b)):
            self.__color = (r, g, b)

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(s, int) and s > 0 for s in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def get_sides(self):
        return self._sides

    def len(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def init(self, color, radius):
        super().init(color, radius)
        self.__radius = self._sides[0]

    def get_square(self):
        return 3.14 * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

class Cube(Figure):
    sides_count = 12

    def init(self, color, side_length):
        super().init(color, side_length)
        self._sides = [self._sides[0]] * self.sides_count

    def get_volume(self):
        return self._sides[0] ** 3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)
print(circle1.get_color())

cube1.set_color(300, 70, 15)
print(cube1.get_color())

# Test side change
cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())

circle1.set_sides(15)
print(circle1.get_sides())  # Output: [15]


print(len(circle1))
print(cube1.get_volume())