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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    characters = create_characters()
    #characterActions = character_action.GetRunActions(30)
    characterActions = character_action.GetRunFullJumpActions(10, 20)
    characterActionOutputList = get_characters_to_follow_actions(characters, characterActions)
    plotting.PlotActions(characterActions, characterActionOutputList)

