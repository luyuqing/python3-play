class Some():
    interface = 1
    _internal = 2  # does not import objects whose name starts with an underscore
    __private = 3

    def __init__(self):
        self.pp = Some.__private  # inside class still use __private

print(Some._Some__private)  # 3  #outside use _Some_private


"""property"""

class Some2():
    def __init__(self, num):
        self.val = num

    @property
    def mul(self):
        return self.val**2


s = Some2(5)
print(s.mul)  # 25


"""getter and setter"""
# disallow to set negative values on width, height, and starts from __init__ phase


class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height
