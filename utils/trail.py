import pygame


class Trail(object):
    '''Object to draw a trail of line segments between a moving point.'''


    def __init__(self, color: tuple[int, int, int], length: int = 16, resolution: int = 2) -> None:
        '''
        Initializes the tail object.

        Parameters
        - color:      the RGB color of the trail
        - length:     the maximum number of line segments composing this trail
        - resolution: milliseconds to add new line segments
        '''
        super().__init__()
        self._length = length
        self._res    = resolution
        self._color  = color
        self.clear()


    def update(self, dt: int, pos: tuple[int, int]) -> None:
        '''
        Call this every update.
        
        Parameters
        - dt:  delta time; the number of ms between game updates
        - pos: the position of the object that generates the trail
        '''

        # add line segments every _res milliseconds
        self._time += dt
        if self._time >= self._res:

            # reset timer & add line segment
            self._time = 0
            self._points.append(pos)

            # remove oldest line segment when trail exceeds max length
            if len(self._points) > self._length:
                self._points.pop(0)


    def draw(self, surface: pygame.Surface) -> None:
        '''
        Draws trail to surface.

        Parameters
        - surface: the surface on which to draw line segments
        '''

        # pygame.draw.lines requires at least 2 points
        if len(self._points) > 1:
            pygame.draw.lines(surface, self._color, False, self._points, width=4)

    def clear(self) -> None:
        '''Call this to clear all line segments in trail.'''
        self._points = []
        self._time = 0