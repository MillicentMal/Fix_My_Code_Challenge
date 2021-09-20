#!/usr/bin/python3
"""Square operations
"""

class Square():
    """"creates square and sets width and height"""     
    width = 0
    height = 0
    def __init__(self, *args, **kwargs):
        """sets square attributes"""
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """calculates perimeter"""
        return (self.width * 2) + (self.height * 2)
    
    def __str__(self):
        """return square format"""
        return "{}*{}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
