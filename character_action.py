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

HAX_STICK_POSITION = 1.0
HUMAN_STICK_POSITION = 0.9875

class ActionType(Enum):
    NONE = 0
    RUN = 1
    FULLJUMP = 2
    SHORTHOP = 3
    WAVEDASH = 4

class JumpType(Enum):
    NONE = 0
    JUMPSQUAT = 1
    FULLJUMP = 2
    SHORTHOP = 3

class CharacterAction(object):
    Action = ActionType.NONE
    Run = False
    Jump = JumpType.NONE
    DashRunStickPosition = HAX_STICK_POSITION
    LastSquatFrameStickPosition = HAX_STICK_POSITION # This can determine if the forward or back jump animation plays, and the velocity on the first jump frame
    AerialDriftStickPosition = HAX_STICK_POSITION
    ActionLength = 20
    
    def __init__(self, action, length):
        self.Action = action
        self.ActionLength = length
            

    def SetFromCharacterAction(self, action):
        self.WaveDash = action.WaveDash
        self.Run = action.Run
        self.Jump = action.Jump
        self.DashRunStickPosition = action.DashRunStickPosition
        self.LastSquatFrameStickPosition = action.LastSquatFrameStickPosition
        self.WaAerialDriftStickPositionveDash = action.AerialDriftStickPosition
        self.FastFall = action.WaveDash

def GetRunActions(runLength):
    characterActionsList = []
    characterActionsList.append(CharacterAction(ActionType.RUN, runLength))
    return characterActionsList

def GetRunFullJumpActions(runLength, jumpLength):
    characterActionsList = []
    characterActionsList.append(CharacterAction(ActionType.RUN, runLength))
    characterActionsList.append(CharacterAction(ActionType.FULLJUMP, jumpLength))
    return characterActionsList


class CharacterActionOutput(object):
    
    def get_last_velocity(self):
        if len(self.VelocityArray) > 0:
            return self.VelocityArray[-1]
        return 0
    
    def get_last_distance(self):
        if len(self.DistanceArray) > 0:
            return self.DistanceArray[-1]
        return 0

    def __init__(self, character):
        self.Character = character
        self.VelocityArray = []
        self.DistanceArray = []
