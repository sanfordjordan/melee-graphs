"""
Change all this to new input - an array with the inputs for each frame:
[
    [1.0, 0.0, 0, 0],
    [0.9875, 0.015, 1, 0],
    [-0.5, -0.5, 1, 1]
]
Each frame has inputs for [<stick position x>, <stick position y>, <jump pressed>, <shield pressed>]
"""

class Inputs(object):
    self.input = [[]]

    def SetFromInput(self, input):
        self.input = input


def GetRunSquatCharacterAction():
    characterAction = CharacterAction()
    characterAction.Run = True
    characterAction.Jump = JumpType.JUMPSQUAT
    return characterAction

def GetRunFullJumpCharacterAction():
    characterInput = [
        [1.0, 0.0, 0, 0], [0.9875, 0.015, 1, 0],[-0.5, -0.5, 1, 1]
    ]
    return characterInput


class CharacterActionOutput(object):
    
    def get_last_velocity(self):
        if len(self.VelocityArray) > 0:
            return self.VelocityArray[-1]
        return 0

    def __init__(self, character):
        self.Character = character.CharacterNameEnum
        self.VelocityArray = []
        self.distance = []
