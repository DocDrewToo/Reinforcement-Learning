import random

gamma = 0.9
epsilon = 0.1
chance_to_drift_right = 0.1
chance_to_drift_left = 0.1

total_visits_table = {}

q_value_table = {}

valid_starting_positions = ("B2", "B3", "B4", "B5",
                            "C3", "C4", "C6",
                            "D3", "D6",
                            "E2", "E3", "E4", "E5", "E6",
                            )

initial_rewards_table = {
    "A1": -50, "A2": -50, "A3": -50, "A4": -50, "A5": -50, "A6": -50, "A7": -50,
    "B1": -50, "B2": 0, "B3": 0, "B4": 0, "B5": 0, "B6": "WALL", "B7": -50,
    "C1": -50, "C2": "WALL", "C3": 0, "C4": 0, "C5": "WALL", "C6": 0, "C7": -50,
    "D1": -50, "D2": "WALL", "D3": 0, "D4": 100, "D5": "WALL", "D6": 0, "D7": -50,
    "E1": -50, "E2": 0, "E3": 0, "E4": 0, "E5": 0, "E6": 0, "E7": -50,
    "F1": -50, "F2": -50, "F3": -50, "F4": -50, "F5": -50, "F6": -50, "F7": -50,
}

reward_for_move = {
    "NORTH": -3,
    "SOUTH": -1,
    "EAST": -2,
    "WEST": -2
}

directions = ("NORTH",
              "SOUTH",
              "EAST",
              "WEST")


def starting_position():
    return random.choice(valid_starting_positions)


def best_direction_to_move(position):
    best_direction = ""
    # Use max q for best direction, unless hit by randomness introduced by epsilon
    if random.random() <= epsilon:
        best_direction = random.choice(directions)
        print("Random direction triggered! for Position: ", position,
              "Now heading ", best_direction)
        return best_direction

    max_q_value = get_max_q_value(position)

    # Translate the numeric value of max q position to an actual direction (N,S,E,W)
    # Example q_values array from q_value_table.get(position):
    # {"NORTH": 2, "SOUTH": 50, "EAST": 5, "WEST": 2}
    directions_at_position_list = list(q_value_table.get(position).keys())
    q_values_at_position_list = list(q_value_table.get(position).values())
    index_of_max_q_value = q_values_at_position_list.index(max_q_value)
    # Now that we have the index of the max_q value, it's the same as the index
    # of the list of direction. Return the direction as a string.
    best_direction = directions_at_position_list[index_of_max_q_value]

    return best_direction


def get_max_q_value(position):
    all_directions_at_position = q_value_table.get(position)

    # TODO iterate through directions
    q_values_all_directions = [
        all_directions_at_position.get(directions[0]),
        all_directions_at_position.get(directions[1]),
        all_directions_at_position.get(directions[2]),
        all_directions_at_position.get(directions[3])
    ]
    return max(q_values_all_directions)


def calculate_q_value(current_position, current_direction, future_position, future_direction):
    current_state_q = q_value_table.get(current_position).get(current_direction)
    how_many_times_this_direction = total_visits_table.get(current_position).get(current_direction)

    number_of_tries_ratio = 1 / (1 + how_many_times_this_direction)
    current_action_reward = reward_for_move.get(current_direction)

    max_future_q_value = get_max_q_value(future_position)

    gamma_probability = current_state_q + number_of_tries_ratio * \
                        (current_action_reward + gamma *
                         max_future_q_value - current_state_q)
    return gamma_probability

def headed_this_way_to_the_left_is(direction):
    to_the_left_is = direction
    if direction == "NORTH":
        to_the_left_is = "WEST"
    elif direction == "EAST":
        to_the_left_is = "NORTH"
    elif direction == "SOUTH":
        to_the_left_is = "EAST"
    elif direction == "WEST":
        to_the_left_is = "SOUTH"

    return to_the_left_is

def headed_this_way_to_the_right_is(direction):
    to_the_right_is = direction
    if direction == "NORTH":
        to_the_right_is = "EAST"
    elif direction == "EAST":
        to_the_right_is = "SOUTH"
    elif direction == "SOUTH":
        to_the_right_is = "WEST"
    elif direction == "WEST":
        to_the_right_is = "NORTH"

    return to_the_right_is

def next_position_with_drift(position_in_maze, direction):
    next_position = position_in_maze
    # if random.random() <= chance_to_drift_right:
    #     next_position = left_from_here()
    # if random.random() >= 1 - chance_to_drift_left:
    #     next_position = right_from_here()

    #Position has the format of letters for columns and numnbers for rows
    # i.e. A3 is row A column 3.
    characters_in_position_location = []
    for character in position_in_maze:
        characters_in_position_location.append(character)
    
    current_row = characters_in_position_location[0]
    current_column = characters_in_position_location[1]

    new_row = current_row
    new_column = int(current_column)
    if direction == "NORTH":
        # ok, this magic of chr and ord, converts letters to numbers
        # perform mathc, then converts back to a letter
        new_row = chr(ord(current_row[0]) - 1)
        new_column = current_column
    elif direction == "SOUTH":
        new_row = chr(ord(current_row[0]) + 1)
        new_column = current_column
    elif direction == "EAST":
        new_row = current_row
        new_column = int(current_column) + 1
    elif direction == "WEST":
        new_row = current_row
        new_column = int(current_column) - 1
    
    next_position = new_row+str(new_column)
    
    if initial_rewards_table.get(next_position) == "WALL":
        next_position = position_in_maze
    
    if initial_rewards_table.get(next_position) == -50:
        next_position = "EXIT"

    if initial_rewards_table.get(next_position) == 100:
        next_position = "EXIT"

    return next_position


if __name__ == "__main__":
    # current_position = starting_position()
    # direction_to_move = best_direction_to_move(starting_position)
    # next_position = next_position_with_drift(current_position, direction_to_move)
    print("Hello")
