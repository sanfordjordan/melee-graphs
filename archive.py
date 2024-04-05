"""
def graph_dash_run_terminal_velocity(characters):
    x_name = []
    y_velocity_ground = []
    y_velocity_air = []
    for character in characters:
        x_name.append(character.characterName)
        y_velocity_ground.append(character.dashAndRunTerminalVelocity)
        y_velocity_air.append(character.jumpHMaximumVelocity)

    plt.plot(x_name, y_velocity_ground)
    plt.plot(x_name, y_velocity_air)
    plt.xticks(rotation=90)
    plt.title('Random')
    plt.xlabel('Character name')
    plt.ylabel('value')
    plt.show()
"""

def plot_jump_squat_and_horizontal_aerial_velocity(characters):

    frame_length = 60
    text_position_gap = round(float(frame_length) / len(characters))
    number = 1
    for character in characters:
        jump_squat_frames = get_character_jump_squat_velocity(character, character.dashAndRunTerminalVelocity)
        aerial_frames = get_character_horizontal_aerial_velocity(character, jump_squat_frames[len(jump_squat_frames) - 1], frame_length - len(jump_squat_frames), HAX_STICK_POSITION, HAX_STICK_POSITION)
        jump_and_aerial_frames = jump_squat_frames + aerial_frames

        x_values = range(0, frame_length)
        plt.plot(x_values, jump_and_aerial_frames, label=character.characterName)
        plt.text(number*text_position_gap, jump_and_aerial_frames[number*text_position_gap], character.characterName, rotation=0)
        number = number + 1

        plt.axvline(0)
        plt.text(-0.25, 1, 'JumpSquat Starts', rotation=90)

    plt.legend()
    plt.show()


def plot_frames(frames):

    frame_length = len(frames)

    for character in characters:
        jump_squat_frames = get_character_jump_squat_velocity(character, character.dashAndRunTerminalVelocity)
        aerial_frames = get_character_horizontal_aerial_velocity(character,
                                                                 jump_squat_frames[len(jump_squat_frames) - 1],
                                                                 frame_length - len(jump_squat_frames),
                                                                 HAX_STICK_POSITION, HAX_STICK_POSITION)
        jump_and_aerial_frames = jump_squat_frames + aerial_frames

        x_values = range(0, frame_length)
        plt.plot(x_values, jump_and_aerial_frames, label=character.characterName)
        plt.text(number, jump_and_aerial_frames[number],
                 character.characterName, rotation=0)
        number = number + 1

        plt.axvline(0)
        plt.text(-0.25, 1, 'JumpSquat Starts', rotation=90)

    plt.legend()
    plt.show()


def plot_jump_squat_velocity(characters):

    for character in characters:
        jump_squat_frames = get_character_jump_squat_velocity(character, character.dashAndRunTerminalVelocity)
        x_values = range(0, character.jumpStartup)
        plt.plot(x_values, jump_squat_frames, label=character.characterName)
        plt.text(x_values[character.jumpStartup-1], jump_squat_frames[len(jump_squat_frames) - 1], character.characterName, rotation=0)

        plt.axvline(0)
        plt.text(-0.25, 1, 'JumpSquat Starts', rotation=90)

    plt.legend()
    plt.show()

def get_character_horizontal_aerial_velocity(character, last_jump_squat_velocity, number_of_frames, last_jump_squat_stick_position, aerial_drift_stick_position):

    horizontal_aerial_frames = []

    for frame in range(0, number_of_frames):
        if frame == 0:
            current_velocity = (character.jumpHInitialVelocity * last_jump_squat_stick_position) + (
                        last_jump_squat_velocity * character.groundAirJumpMomentumMultiplier)
            if current_velocity > character.jumpHMaximumVelocity:
                current_velocity = character.jumpHMaximumVelocity
        else:
            current_velocity = current_velocity - character.airFriction
            if (current_velocity < character.maxAerialHVelocity * aerial_drift_stick_position) or (frame >= character.jumpAnimationFrames):
                current_velocity = character.maxAerialHVelocity * aerial_drift_stick_position

        horizontal_aerial_frames.append(current_velocity)

    return horizontal_aerial_frames


def get_character_jump_squat_velocity(character, initial_velocity):
    current_velocity = initial_velocity
    jump_squat_frames = []

    for frame in range(0, character.jumpStartup):
        velocity_drop_multiplier = 1
        if current_velocity > character.walkMaximumVelocity:
            velocity_drop_multiplier = 2

        current_velocity = current_velocity - (velocity_drop_multiplier * character.friction)
        jump_squat_frames.append(current_velocity)

    return jump_squat_frames