import matplotlib.pyplot as plt
from character_action import JumpType
import numpy as np
import pandas as pd

def PlotAction(characterAction, characterActionOutputList):
    #CsvVelocities(characterActionOutputList)
    CsvDistances(characterActionOutputList)
    PlotVelocities(characterAction, characterActionOutputList)
    PlotDistances(characterAction, characterActionOutputList)
    

def Plot(x_values, y_values, plotLabel):
    plt.plot(x_values, y_values, label=plotLabel)
    plt.text(x_values[len(x_values)-1], y_values[len(y_values) - 1], plotLabel, rotation=0)
    
def CsvVelocities(characterActionOutputList):
    csvVelocities = []

    for character in characterActionOutputList:
        character_velocities = [ '%.2f' % elem for elem in character.VelocityArray ]
        character_velocities.insert(0,character.Character.value)
        csvVelocities.append(character_velocities)
        
    arr = np.array(csvVelocities)
    #arr_t = arr.T
    df = pd.DataFrame(arr)
    df.to_csv("velocity_output.csv")
    
def CsvDistances(characterActionOutputList):
    csvDistances = []

    for character in characterActionOutputList:
        character_distances = [ '%.2f' % elem for elem in character.distance ]
        character_distances.insert(0,character.Character.value)
        csvDistances.append(character_distances)
        
    arr = np.array(csvDistances)
    #arr_t = arr.T
    df = pd.DataFrame(arr)
    df.to_csv("distance_output5.csv")

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

