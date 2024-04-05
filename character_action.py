from enum import Enum

"""
Change all this to new input - an array with the inputs for each frame:
[
    [1.0, 0.0, 0, 0],
    [0.9875, 0.015, 1, 0],
    [-0.5, -0.5, 1, 1]
]
Each frame has inputs for [<stick position x>, <stick position y>, <jump pressed>, <shield pressed>]
"""

class JumpType(Enum):
    NONE = 0
    JUMPSQUAT = 1
    FULLJUMP = 2
    SHORTHOP = 3

class CharacterAction(object):
    WaveDash = False
    Run = False
    Jump = JumpType.NONE
    DashRunStickPosition = 1.0
    LastSquatFrameStickPosition = 1.0 # This can determine if the forawrd or back jump animation plays, and the velocity on the first jump frame
    AerialDriftStickPosition = 1.0
    FastFall = False

    def SetFromCharacterAction(self, action):
        self.WaveDash = action.WaveDash
        self.Run = action.Run
        self.Jump = action.Jump
        self.DashRunStickPosition = action.DashRunStickPosition
        self.LastSquatFrameStickPosition = action.LastSquatFrameStickPosition
        self.WaAerialDriftStickPositionveDash = action.AerialDriftStickPosition
        self.FastFall = action.WaveDash


def GetRunSquatCharacterAction():
    characterAction = CharacterAction()
    characterAction.Run = True
    characterAction.Jump = JumpType.JUMPSQUAT
    return characterAction

def GetRunFullJumpCharacterAction():
    characterAction = CharacterAction()
    characterAction.Run = True
    characterAction.Jump = JumpType.FULLJUMP
    return characterAction


class CharacterActionOutput(object):
    
    def get_last_velocity(self):
        if len(self.VelocityArray) > 0:
            return self.VelocityArray[-1]
        return 0

    def __init__(self, character):
        self.Character = character.CharacterNameEnum
        self.VelocityArray = []
        self.distance = []
