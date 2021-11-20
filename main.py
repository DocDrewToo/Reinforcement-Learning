import random
import logging
import os
from print_n_value import print_table as print_n_value_table
from print_optimal_policy import print_table as print_policy_table
from print_q_value import print_table as print_q_value_table

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

gamma = 0.9
epsilon = 0.1
chance_to_drift_right = 0.1
chance_to_drift_left = 0.1

total_visits_table = {
}

q_value_table = {
}

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
    max_q_value = get_max_q_value(position)

    # Use max q for best direction, unless hit by randomness introduced by epsilon
    if random.random() <= epsilon or max_q_value == 0:
        best_direction = random.choice(directions)
        log.debug("   Random direction triggered! (epsilon or zero q value) ")
        log.debug("   Randomily Heading: %s ", best_direction)
        return best_direction

    # Translate the numeric value of max q position to an actual direction (N,S,E,W)
    # Example q_values array from q_value_table.get(position):
    # {"NORTH": 2, "SOUTH": 50, "EAST": 5, "WEST": 2}
    directions_at_position_list = list(q_value_table.get(position).keys())
    q_values_at_position_list = list(q_value_table.get(position).values())
    index_of_max_q_value = q_values_at_position_list.index(max_q_value)
    # Now that we have the index of the max_q value, it's the same as the index
    # of the list of direction. Return the direction as a string.
    best_direction = directions_at_position_list[index_of_max_q_value]
    log.debug("   Best direction to head: %s ", best_direction)

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


def calculate_q_value(current_position, current_direction, future_position):
    current_state_q = q_value_table.get(current_position).get(current_direction)
    how_many_times_this_direction = total_visits_table.get(current_position).get(current_direction)

    number_of_tries_ratio = 1 / (1 + how_many_times_this_direction)
    current_action_reward = reward_for_move.get(current_direction)

    max_future_q_value = get_max_q_value(future_position)

    q_value = current_state_q + number_of_tries_ratio * \
              (current_action_reward + gamma *
               max_future_q_value - current_state_q)

    return q_value


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


def convert_position_plus_direction_to_new_position(position, direction):
    # Takes in a position i.e. B3 and direction i.e. NORTH.
    # Then performs column/row math to get the next position in the maze
    #  when heading the specified direction

    position_to_row_and_column = []
    for character in position:
        position_to_row_and_column.append(character)

    current_row = position_to_row_and_column[0]
    current_column = position_to_row_and_column[1]

    new_row = current_row
    new_column = int(current_column)
    if direction == "NORTH":
        # ok, this magic of chr and ord, converts letters to numbers
        # performs addition or subtraction, then converts back to a letter
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

    return new_row + str(new_column)


def chance_for_direction_changed_by_drift(direction):
    next_direction = direction
    # With a 10% chance to drift left, translated to 0 -> 0.01 from random # generator
    random_number = random.random()
    if random_number <= chance_to_drift_right:
        next_direction = headed_this_way_to_the_left_is(direction)
        log.debug("   Got Struck by drif to the RIGHT, now heading: %s", next_direction)
    # With a 10% chance to drift right, translated to 0.9 -> 1.0 from random # generator
    if random_number >= 1 - chance_to_drift_left:
        next_direction = headed_this_way_to_the_right_is(direction)
        log.debug("   Got Struck by drif to the LEFT, now heading %s", next_direction)

    # Return origonal direction if we weren't struck by 20% randomness
    return next_direction


def get_next_position(position_in_maze, direction):
    next_position = convert_position_plus_direction_to_new_position(position_in_maze, direction)

    # Check initial rewards table to see if next position is a wall or an exit location
    if initial_rewards_table.get(next_position) == "WALL":
        # Bounce back to starting position if a wall is encountered
        log.debug("   Oops, hit a wall")
        next_position = position_in_maze

    return next_position


def update_q_value(position, direction, value):
    q_value_table[position][direction] = value


def update_total_times_this_direction(position, direction):
    how_many_times_this_direction = total_visits_table.get(position).get(direction)
    total_visits_table[position][direction] = how_many_times_this_direction + 1

def preload_total_visits_table():
    for position in initial_rewards_table:
        directional_values = {}
        for direction in directions:
            directional_values[direction] = 0
        total_visits_table[position] = directional_values
    return total_visits_table

def preload_q_value_table():
    for position in initial_rewards_table:
        directional_values = {}
        for direction in directions:
            if initial_rewards_table[position] == "WALL":
                directional_values[direction] = 0
            else:
                directional_values[direction] = initial_rewards_table[position]
        q_value_table[position] = directional_values
    return q_value_table


if __name__ == "__main__":
    log.info("Into the maze we go...!")
    preload_total_visits_table()
    preload_q_value_table()

    # TODO Loop 50,000 times:...
    for total_maze_runs in range(1, 50000):
        log.debug("Starting Trail: %s", total_maze_runs)
        CONTINUE_TRIAL = True
        moves_per_trial = 0
        current_position = starting_position()

        while CONTINUE_TRIAL:
            log.debug("Current Position: %s", current_position)

            direction_to_move = best_direction_to_move(current_position)
            direction_to_move = chance_for_direction_changed_by_drift(direction_to_move)

            log.debug("Moving: %s", direction_to_move)
            next_position = get_next_position(current_position, direction_to_move)

            q_value = calculate_q_value(current_position, direction_to_move, next_position)
            update_q_value(current_position, direction_to_move, q_value)

            update_total_times_this_direction(current_position, direction_to_move)
            moves_per_trial += 1

            # Check if next position is a terminal state
            if initial_rewards_table.get(next_position) == -50 or \
                    initial_rewards_table.get(next_position) == 100 or \
                    moves_per_trial >= 100:
                CONTINUE_TRIAL = False
            else:
                current_position = next_position

        log.debug("Ending Position: %s", next_position)
        log.debug("___________________")

    print_n_value_table(total_visits_table, initial_rewards_table)
    print_q_value_table(q_value_table, initial_rewards_table)
    print_policy_table(q_value_table)
