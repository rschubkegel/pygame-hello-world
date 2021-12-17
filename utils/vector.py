import typing


class Vector2(object):
    '''Container for mutable x and y values.'''


    def __init__(self, *args: typing.Union[float, tuple[float, float]]) -> None:
        '''
        Initialize the object depending on arguments passed.
        If no args provided, x and y are initialized to 0.
        If two floats are provided, x and y are initialized to those respective values.
        If one tuple is provided, it will be unpacked into x and y values.'''
        super().__init__()

        # no args, initialize to 0,0
        if len(args) == 0:
            self._x = self._y = 0

        # can initialize with seperate x, y values
        elif len(args) == 2:
            self._x = args[0]
            self._y = args[1]

        # can also initialize with tuple
        else:
            self._x, self._y = args[0]


    def get_x(self) -> float:
        return self._x


    def set_x(self, x) -> None:
        self._x = x


    def del_x(self) -> None:
        del self._x

    def doc_x(self) -> str:
        return 'Represents the x coordinate of the vector'


    x = property(get_x, set_x, del_x, doc_x)


    def get_y(self) -> float:
        return self._y


    def set_y(self, y) -> None:
        self._y = y


    def del_y(self) -> None:
        del self._y

    def doc_y(self) -> str:
        return 'Represents the y coordinate of the vector'


    y = property(get_y, set_y, del_y, doc_y)