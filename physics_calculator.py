from character_action import JumpType, CharacterActionOutput
import numpy as np

# get_character_to_follow actions
def charcter_plays_actions(character, inputs):
    characterActionOutput = CharacterActionOutput(character)



    return characterActionOutput

def get_character_to_follow_action(character, characterAction):
    characterActionOutput = CharacterActionOutput(character)
    
    if(characterAction.Run):
        get_run_velocities(character, characterAction, characterActionOutput)
    
    if(characterAction.Jump != JumpType.NONE):
        get_jumpsquat_velocities(character, characterActionOutput)

    if(characterAction.Jump == JumpType.FULLJUMP
            or characterAction.Jump == JumpType.SHORTHOP):
        get_air_velocities(character, characterAction, characterActionOutput)

    characterActionOutput.distance = get_distance_travelled(characterActionOutput)

    return characterActionOutput

def get_run_velocities(character, characterAction, characterActionOutput):
    # todo: Have velocity of frames leading up to terminal run velocity - for now just have terminal velocity.
    # Run for 10 frames
    for frame in range(0, 10):
        velocity = characterActionOutput.get_last_velocity()
        # First frame of dash is the same velocity as whatever the previous frames velocity was
        # e.g. if wavedashed and previous frame speed was 1.4 - the first frame of dash speed is 1.4
        if frame == 0:
            characterActionOutput.VelocityArray.append(velocity)
            continue

        if frame == 1:
            # Default starting dash speed if dashInitialVelocity is same as dashAndRunTerminalVelocity
            velocity = character.dashInitialVelocity
    
        velocity_smaller = velocity - character.friction
        velocity_larger = velocity + (character.dashAndRunAccelerationA * characterAction.DashRunStickPosition) + character.dashAndRunAccelerationB

        # Lower dashInitialVelocity if it is higher than dashAndRunTerminalVelocity
        if (velocity > character.dashAndRunTerminalVelocity):
            velocity = max(velocity_smaller, character.dashAndRunTerminalVelocity)

        # Increase dashInitialVelocity if it is lower than dashAndRunTerminalVelocity
        elif (velocity < character.dashAndRunTerminalVelocity):
            velocity = min(velocity_larger, character.dashAndRunTerminalVelocity)

        characterActionOutput.VelocityArray.append(velocity)

    return


def get_jumpsquat_velocities(character, characterActionOutput):
    # Should be grounded for jumpsquat
    for frame in range(0, character.jumpStartup):
        currentVelocity = characterActionOutput.get_last_velocity()

        # Friction amount depends on current speed
        frictionMultiplier = 1
        if abs(currentVelocity) > character.walkMaximumVelocity:
            frictionMultiplier = 2

        # Shrink speed due to friction
        friction_applied = abs(currentVelocity) - (frictionMultiplier * character.friction)
        # Ensure friction will not make you go backwards - also apply original direction of movement
        new_velocity = friction_applied * np.sign(currentVelocity) if friction_applied > 0 else 0

        characterActionOutput.VelocityArray.append(new_velocity)
    return

def get_air_velocities(character, characterAction, characterActionOutput):

    # Ensure last frame velocity was from jumpsquat
    lastSquatFrameVelocity = characterActionOutput.get_last_velocity()
    lastSquatFrameStickPosition = characterAction.LastSquatFrameStickPosition
    aerialDriftStickPosition = characterAction.AerialDriftStickPosition
    number_of_frames = 70

    for frame in range(0, number_of_frames):
        if frame == 0:
            # This is technically incorrect if the lastSquatFrameStickPosition is pointing opposite way (and gets jump back animation)
            # or perhaps even if stick value is less than 0.2875 ?
            ground_air_momentum = (lastSquatFrameVelocity * character.groundAirJumpMomentumMultiplier)
            potential_start_velocity = (character.jumpHInitialVelocity * lastSquatFrameStickPosition) + ground_air_momentum
            current_velocity = min(potential_start_velocity, character.jumpHMaximumVelocity)
        else:
            current_velocity = current_velocity - character.airFriction
            # aerialDriftStickPosition may round down to 0 if stick is 0.2875 > x > -0.2875 ?
            if (current_velocity < character.maxAerialHVelocity * aerialDriftStickPosition) or (frame >= character.jumpAnimationFrames):
                current_velocity = character.maxAerialHVelocity * aerialDriftStickPosition

        characterActionOutput.VelocityArray.append(current_velocity)

    return


def get_distance_travelled(characterActionOutput):
    velocity_array = characterActionOutput.VelocityArray
    distance = []
    total_distance = 0
    for velocity in velocity_array:
        total_distance += velocity
        distance.append(total_distance)

    return distance

