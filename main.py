import matplotlib.pyplot as plt
from labellines import labelLine, labelLines

from character_context import create_characters
import plotting
import character_action
import physics_calculator

def get_characters_to_follow_actions(characters, characterActions):
    characterActionOutputList = []
    for character in characters:
        characterActionOutput = physics_calculator.get_character_to_follow_actions(character, characterActions)
        characterActionOutputList.append(characterActionOutput)

    return characterActionOutputList

def CompleteSingleCharacterActions():
    #characterActions = character_action.GetRunActions(30)
    characterActions = character_action.GetRunFullJumpActions(10, 20)
    characterActionOutputList = get_characters_to_follow_actions(characters, characterActions)
    plotting.PlotActions(characterActions, characterActionOutputList)

def CompleteMultipleCharacterActions():
    finalList = []
    for runLength in range(0,12):
        characterActions = character_action.GetRunFullJumpActions(runLength, 30-runLength)
        characterActionOutputList = get_characters_to_follow_actions(characters, characterActions)
        finalList.append(characterActionOutputList)
        
    characterActionOutputList = []
    for characterIndex in range(0, len(finalList[0]) - 1):
        characterVelocityList = []
        characterDistanceList = []
        for runIndex in range(0, len(finalList) - 1):
            characterVelocityList.append(finalList[runIndex][characterIndex].VelocityArray[-1])
            characterDistanceList.append(finalList[runIndex][characterIndex].DistanceArray[-1])
            
        characterActionOutput = character_action.CharacterActionOutput(finalList[runIndex][characterIndex].Character)
        characterActionOutput.VelocityArray = characterVelocityList
        characterActionOutput.DistanceArray = characterDistanceList
        characterActionOutputList.append(characterActionOutput)
    
    plotting.PlotActions(characterActionOutputList, characterActionOutputList)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    characters = create_characters()
    CompleteMultipleCharacterActions()