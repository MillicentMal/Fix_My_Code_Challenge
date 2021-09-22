#!/usr/bin/python3
"""Square operations
"""

class Square():
    """"creates square and sets width and height"""     
    width = 0
    
    def __init__(self, *args, **kwargs):
        """sets square attributes"""
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def permiter_of_my_square(self):
        """calculates perimeter"""
        return (self.width * 2 + self.width * 2) 
    
    def __str__(self):
        """return square format"""
        return "{}/{}".format(self.width, self.width)


if __name__ == "__main__":
    s = Square(width=12, height)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
