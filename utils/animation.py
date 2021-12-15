from typing import Sized
from pygame import Surface


class Animation(Sized):
    '''
    Holds frames for an animation as well as some metadata.
    '''


    def __init__(self, frames: list[Surface], looping: bool = True) -> None:
        '''
        Initializes the animation.

        Parameters
        - frames:  a list of frames in this animation
        - looping: if true, the current frame will be set to the first frame
                   after the end of the animation is reached;
                   otherwise, the current frame will be the last frame of the
                   animation until it is explicitly reset
        '''

        self.frames = frames
        self.looping = looping


    def __getitem__(self, index: int) -> Surface:
        '''
        Returns the frame of the animation at the specified index.

        Parameters
        - index: the frame of the animation to return
        '''

        return self.frames[index]


    def __len__(self) -> int:
        '''Returns the number of frames in this animation.'''
        return len(self.frames)