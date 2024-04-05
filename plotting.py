import matplotlib.pyplot as plt
from character_action import JumpType

def PlotAction(characterAction, characterActionOutputList):
    PlotVelocities(characterAction, characterActionOutputList)
    PlotDistances(characterAction, characterActionOutputList)

def Plot(x_values, y_values, plotLabel):
    plt.plot(x_values, y_values, label=plotLabel)
    plt.text(x_values[len(x_values)-1], y_values[len(y_values) - 1], plotLabel, rotation=0)

def PlotVelocities(characterAction, characterActionOutputList):

    for character in characterActionOutputList:
        x_values = range(0, len(character.VelocityArray))
        y_values = character.VelocityArray
        
        Plot(x_values, y_values, character.Character.value)

        print(character.Character.value)
        print(y_values)

    plt.title(get_title(characterAction))
    plt.xlabel('Frames')
    plt.ylabel('Velocity')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def PlotDistances(characterAction, characterActionOutputList):

    for character in characterActionOutputList:
        x_values = range(0, len(character.distance))
        y_values = character.distance

        Plot(x_values, y_values, character.Character.value)

    plt.title(get_title(characterAction))
    plt.xlabel('Frames')
    plt.ylabel('Distance')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

def get_title(characterAction):
    title = "Characters"
    if(characterAction.Run): title += " Run"
    if(characterAction.Jump == JumpType.JUMPSQUAT): title += " & JumpSquat"
    if(characterAction.Jump == JumpType.FULLJUMP): title += " & FullJump"
    if(characterAction.Jump == JumpType.SHORTHOP): title += " & ShortHop"
    return title

"""
def plot_dividers(characterAction):
    if(characterAction.Jump != CharacterAction.JumpType.NONE):
        plt.axvline(0)
        plt.text(-0.25, 1, 'JumpSquat Starts', rotation=90)
"""

