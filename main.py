import matplotlib.pyplot as plt
from labellines import labelLine, labelLines

from character_context import create_characters
import plotting
import character_action
import physics_calculator

def get_characters_to_follow_action(characters, characterAction):
    characterActionOutputList = []
    for character in characters:
        characterActionOutput = physics_calculator.get_character_to_follow_action(character, characterAction)
        characterActionOutputList.append(characterActionOutput)

    return characterActionOutputList


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    characters = create_characters()
    characterAction = character_action.GetRunFullJumpCharacterAction()
    characterActionOutputList = get_characters_to_follow_action(characters, characterAction)
    plotting.PlotAction(characterAction, characterActionOutputList)

    #plot_jump_squat_velocity(characters)
    #plot_jump_squat_and_horizontal_aerial_velocity(characters)
    #graph_dash_run_terminal_velocity(characters)

