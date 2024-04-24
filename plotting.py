import matplotlib.pyplot as plt
from character_action import ActionType, JumpType
import numpy as np
import pandas as pd
from datetime import datetime

def PlotActions(characterActions, characterActionOutputList):
    CsvVelocities(characterActionOutputList)
    CsvDistances(characterActionOutputList)
    PlotVelocities(characterActions, characterActionOutputList)
    PlotDistances(characterActions, characterActionOutputList)
    

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
    df.to_csv("velocity_output_" + GetDateTimeString() + ".csv")
    
def CsvDistances(characterActionOutputList):
    csvDistances = []

    for character in characterActionOutputList:
        character_distances = [ '%.2f' % elem for elem in character.DistanceArray ]
        character_distances.insert(0,character.Character.value)
        csvDistances.append(character_distances)
        
    arr = np.array(csvDistances)
    #arr_t = arr.T
    df = pd.DataFrame(arr)
    df.to_csv("distance_output_" + GetDateTimeString() + ".csv")

def PlotVelocities(characterActions, characterActionOutputList):

    for character in characterActionOutputList:
        x_values = range(0, len(character.VelocityArray))
        y_values = character.VelocityArray
        
        Plot(x_values, y_values, character.Character.value)

        print(character.Character.value)
        print(y_values)

    plt.title(get_title(characterActions))
    plt.xlabel('Frames')
    plt.ylabel('Velocity')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    
    

def PlotDistances(characterActions, characterActionOutputList):

    for character in characterActionOutputList:
        x_values = range(0, len(character.DistanceArray))
        y_values = character.DistanceArray

        Plot(x_values, y_values, character.Character.value)

    plt.title(get_title(characterActions))
    plt.xlabel('Frames')
    plt.ylabel('Distance')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()
    
    

def get_title(actions):
    title = "Characters"
    for action in actions:
        if(action.Action == ActionType.RUN): title += " Run"
        if(action.Action == ActionType.FULLJUMP): title += " & Jump"
    return title

def GetDateTimeString():
    now = datetime.now()
    return now.strftime("%Y%m%d_%H%M%S")

"""
def plot_dividers(characterAction):
    if(characterAction.Jump != CharacterAction.JumpType.NONE):
        plt.axvline(0)
        plt.text(-0.25, 1, 'JumpSquat Starts', rotation=90)
"""

