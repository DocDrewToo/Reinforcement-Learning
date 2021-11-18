import random
from tkinter import *

gamma = 0.9
epsilon = 0.1
chance_to_drift_right = 0.1
chance_to_drift_left = 0.1

total_visits_table = {
    "A1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "A7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F1": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "F7": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
}

q_value_table = {
    "A1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A2": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A3": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A4": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A5": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A6": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "A7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "B1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "B2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "B7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "C1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "C2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "C7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "D1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "D2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D4": {"NORTH": 100, "SOUTH": 100, "EAST": 100, "WEST": 100},
    "D5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "D7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "E1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "E2": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E3": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E4": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E5": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E6": {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0},
    "E7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F1": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F2": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F3": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F4": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F5": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F6": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50},
    "F7": {"NORTH": -50, "SOUTH": -50, "EAST": -50, "WEST": -50}
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
        print("   Random direction triggered! (epsilon or zero q value)", best_direction)
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
        print("   Got Struck by drif to the RIGHT, wanted to go,", direction, "Ended up going,", next_direction)
    # With a 10% chance to drift right, translated to 0.9 -> 1.0 from random # generator
    if random_number >= 1 - chance_to_drift_left:
        next_direction = headed_this_way_to_the_right_is(direction)
        print("   Got Struck by drif to the LEFT, wanted to go,", direction, "Ended up going,", next_direction)

    # Return origonal direction if we weren't struck by 20% randomness
    return next_direction


def get_next_position(position_in_maze, direction):
    next_position = convert_position_plus_direction_to_new_position(position_in_maze, direction)

    # Check initial rewards table to see if next position is a wall or an exit location
    if initial_rewards_table.get(next_position) == "WALL":
        # Bounce back to starting position if a wall is encountered
        print("   Oops, hit a wall")
        next_position = position_in_maze

    return next_position


def update_q_value(position, direction, value):
    q_value_table[position][direction] = value


def update_total_times_this_direction(position, direction):
    how_many_times_this_direction = total_visits_table.get(position).get(direction)
    total_visits_table[position][direction] = how_many_times_this_direction + 1


if __name__ == "__main__":
    print("Into the maze we go...!")

    # TODO Loop 50,000 times:...
    for total_maze_runs in range(1, 10):
        print("Starting Trail:", total_maze_runs)
        CONTINUE_TRIAL = True
        moves_per_trial = 0
        current_position = starting_position()

        while CONTINUE_TRIAL:
            print("Current Position: ", current_position)

            direction_to_move = best_direction_to_move(current_position)
            direction_to_move = chance_for_direction_changed_by_drift(direction_to_move)

            print("Moving: ", direction_to_move)
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

        print("Ending Position: ", next_position)
        print("___________________")

    #print(q_value_table["A2"]["NORTH"])
    # print("___________________")
    # print(total_visits_table)

visual_maze = Tk()
visual_maze.title("Windy Maze Q-Learning Values")


Q_value_A1 = Label(visual_maze, text=q_value_table["A1"]["NORTH"], padx=10, pady=10)
Q_value_A2 = Label(visual_maze, text=q_value_table["A2"]["NORTH"], padx=10, pady=10)
Q_value_A3 = Label(visual_maze, text=q_value_table["A3"]["NORTH"], padx=10, pady=10)
Q_value_A4 = Label(visual_maze, text=q_value_table["A4"]["NORTH"], padx=10, pady=10)
Q_value_A5 = Label(visual_maze, text=q_value_table["A5"]["NORTH"], padx=10, pady=10)
Q_value_A6 = Label(visual_maze, text=q_value_table["A6"]["NORTH"], padx=10, pady=10)
Q_value_A7 = Label(visual_maze, text=q_value_table["A7"]["NORTH"], padx=10, pady=10)

Q_value_B1 = Label(visual_maze, text=q_value_table["B1"]["NORTH"], padx=10, pady=10)
Q_value_B2_W = Label(visual_maze, text=q_value_table["B2"]["WEST"], padx=10, pady=10)
Q_value_B2_N = Label(visual_maze, text=q_value_table["B2"]["NORTH"], padx=10, pady=10)
Q_value_B2_E = Label(visual_maze, text=q_value_table["B2"]["EAST"], padx=10, pady=10)
Q_value_B2_S = Label(visual_maze, text=q_value_table["B2"]["SOUTH"], padx=10, pady=10)
Q_value_B3_W = Label(visual_maze, text=q_value_table["B3"]["WEST"], padx=10, pady=10)
Q_value_B3_N = Label(visual_maze, text=q_value_table["B3"]["NORTH"], padx=10, pady=10)
Q_value_B3_E = Label(visual_maze, text=q_value_table["B3"]["EAST"], padx=10, pady=10)
Q_value_B3_S = Label(visual_maze, text=q_value_table["B3"]["SOUTH"], padx=10, pady=10)
Q_value_B4_W = Label(visual_maze, text=q_value_table["B4"]["WEST"], padx=10, pady=10)
Q_value_B4_N = Label(visual_maze, text=q_value_table["B4"]["NORTH"], padx=10, pady=10)
Q_value_B4_E = Label(visual_maze, text=q_value_table["B4"]["EAST"], padx=10, pady=10)
Q_value_B4_S = Label(visual_maze, text=q_value_table["B4"]["SOUTH"], padx=10, pady=10)
Q_value_B5_W = Label(visual_maze, text=q_value_table["B5"]["WEST"], padx=10, pady=10)
Q_value_B5_N = Label(visual_maze, text=q_value_table["B5"]["NORTH"], padx=10, pady=10)
Q_value_B5_E = Label(visual_maze, text=q_value_table["B5"]["EAST"], padx=10, pady=10)
Q_value_B5_S = Label(visual_maze, text=q_value_table["B5"]["SOUTH"], padx=10, pady=10)
B6_Wall = Label(visual_maze, text=initial_rewards_table["B6"], padx=10, pady=10)
Q_value_B7 = Label(visual_maze, text=q_value_table["B7"]["NORTH"], padx=10, pady=10)

Q_value_C1 = Label(visual_maze, text=q_value_table["C1"]["NORTH"], padx=10, pady=10)
C2_Wall = Label(visual_maze, text=initial_rewards_table["C2"], padx=10, pady=10)
Q_value_C3_W = Label(visual_maze, text=q_value_table["C3"]["WEST"], padx=10, pady=10)
Q_value_C3_N = Label(visual_maze, text=q_value_table["C3"]["NORTH"], padx=10, pady=10)
Q_value_C3_E = Label(visual_maze, text=q_value_table["C3"]["EAST"], padx=10, pady=10)
Q_value_C3_S = Label(visual_maze, text=q_value_table["C3"]["SOUTH"], padx=10, pady=10)
Q_value_C4_W = Label(visual_maze, text=q_value_table["C4"]["WEST"], padx=10, pady=10)
Q_value_C4_N = Label(visual_maze, text=q_value_table["C4"]["NORTH"], padx=10, pady=10)
Q_value_C4_E = Label(visual_maze, text=q_value_table["C4"]["EAST"], padx=10, pady=10)
Q_value_C4_S = Label(visual_maze, text=q_value_table["C4"]["SOUTH"], padx=10, pady=10)
C5_Wall = Label(visual_maze, text=initial_rewards_table["C5"], padx=10, pady=10)
Q_value_C6_W = Label(visual_maze, text=q_value_table["C6"]["WEST"], padx=10, pady=10)
Q_value_C6_N = Label(visual_maze, text=q_value_table["C6"]["NORTH"], padx=10, pady=10)
Q_value_C6_E = Label(visual_maze, text=q_value_table["C6"]["EAST"], padx=10, pady=10)
Q_value_C6_S = Label(visual_maze, text=q_value_table["C6"]["SOUTH"], padx=10, pady=10)
Q_value_C7 = Label(visual_maze, text=q_value_table["C7"]["NORTH"], padx=10, pady=10)

Q_value_D1 = Label(visual_maze, text=q_value_table["D1"]["NORTH"], padx=10, pady=10)
D2_Wall = Label(visual_maze, text=initial_rewards_table["D2"], padx=10, pady=10)
Q_value_D3_W = Label(visual_maze, text=q_value_table["D3"]["WEST"], padx=10, pady=10)
Q_value_D3_N = Label(visual_maze, text=q_value_table["D3"]["NORTH"], padx=10, pady=10)
Q_value_D3_E = Label(visual_maze, text=q_value_table["D3"]["EAST"], padx=10, pady=10)
Q_value_D3_S = Label(visual_maze, text=q_value_table["D3"]["SOUTH"], padx=10, pady=10)
Q_value_D4_goal = Label(visual_maze, text=q_value_table["D4"]["NORTH"], padx=10, pady=10)
D5_Wall = Label(visual_maze, text=initial_rewards_table["D5"], padx=10, pady=10)
Q_value_D6_W = Label(visual_maze, text=q_value_table["D6"]["WEST"], padx=10, pady=10)
Q_value_D6_N = Label(visual_maze, text=q_value_table["D6"]["NORTH"], padx=10, pady=10)
Q_value_D6_E = Label(visual_maze, text=q_value_table["D6"]["EAST"], padx=10, pady=10)
Q_value_D6_S = Label(visual_maze, text=q_value_table["D6"]["SOUTH"], padx=10, pady=10)
Q_value_D7 = Label(visual_maze, text=q_value_table["D7"]["NORTH"], padx=10, pady=10)

Q_value_E1 = Label(visual_maze, text=q_value_table["E1"]["NORTH"], padx=10, pady=10)
Q_value_E2_W = Label(visual_maze, text=q_value_table["E2"]["WEST"], padx=10, pady=10)
Q_value_E2_N = Label(visual_maze, text=q_value_table["E2"]["NORTH"], padx=10, pady=10)
Q_value_E2_E = Label(visual_maze, text=q_value_table["E2"]["EAST"], padx=10, pady=10)
Q_value_E2_S = Label(visual_maze, text=q_value_table["E2"]["SOUTH"], padx=10, pady=10)
Q_value_E3_W = Label(visual_maze, text=q_value_table["E3"]["WEST"], padx=10, pady=10)
Q_value_E3_N = Label(visual_maze, text=q_value_table["E3"]["NORTH"], padx=10, pady=10)
Q_value_E3_E = Label(visual_maze, text=q_value_table["E3"]["EAST"], padx=10, pady=10)
Q_value_E3_S = Label(visual_maze, text=q_value_table["E3"]["SOUTH"], padx=10, pady=10)
Q_value_E4_W = Label(visual_maze, text=q_value_table["E4"]["WEST"], padx=10, pady=10)
Q_value_E4_N = Label(visual_maze, text=q_value_table["E4"]["NORTH"], padx=10, pady=10)
Q_value_E4_E = Label(visual_maze, text=q_value_table["E4"]["EAST"], padx=10, pady=10)
Q_value_E4_S = Label(visual_maze, text=q_value_table["E4"]["SOUTH"], padx=10, pady=10)
Q_value_E5_W = Label(visual_maze, text=q_value_table["E5"]["WEST"], padx=10, pady=10)
Q_value_E5_N = Label(visual_maze, text=q_value_table["E5"]["NORTH"], padx=10, pady=10)
Q_value_E5_E = Label(visual_maze, text=q_value_table["E5"]["EAST"], padx=10, pady=10)
Q_value_E5_S = Label(visual_maze, text=q_value_table["E5"]["SOUTH"], padx=10, pady=10)
Q_value_E6_W = Label(visual_maze, text=q_value_table["E6"]["WEST"], padx=10, pady=10)
Q_value_E6_N = Label(visual_maze, text=q_value_table["E6"]["NORTH"], padx=10, pady=10)
Q_value_E6_E = Label(visual_maze, text=q_value_table["E6"]["EAST"], padx=10, pady=10)
Q_value_E6_S = Label(visual_maze, text=q_value_table["E6"]["SOUTH"], padx=10, pady=10)
Q_value_E7 = Label(visual_maze, text=q_value_table["E7"]["NORTH"], padx=10, pady=10)

Q_value_F1 = Label(visual_maze, text=q_value_table["F1"]["NORTH"], padx=10, pady=10)
Q_value_F2 = Label(visual_maze, text=q_value_table["F2"]["NORTH"], padx=10, pady=10)
Q_value_F3 = Label(visual_maze, text=q_value_table["F3"]["NORTH"], padx=10, pady=10)
Q_value_F4 = Label(visual_maze, text=q_value_table["F4"]["NORTH"], padx=10, pady=10)
Q_value_F5 = Label(visual_maze, text=q_value_table["F5"]["NORTH"], padx=10, pady=10)
Q_value_F6 = Label(visual_maze, text=q_value_table["F6"]["NORTH"], padx=10, pady=10)
Q_value_F7 = Label(visual_maze, text=q_value_table["F7"]["NORTH"], padx=10, pady=10)

Q_value_A1.grid(row=1, column=2)
Q_value_A2.grid(row=1, column=5)
Q_value_A3.grid(row=1, column=8)
Q_value_A4.grid(row=1, column=11)
Q_value_A5.grid(row=1, column=14)
Q_value_A6.grid(row=1, column=17)
Q_value_A7.grid(row=1, column=20)

Q_value_B1.grid(row=4, column=2)
Q_value_B2_W.grid(row=4, column=4)
Q_value_B2_N.grid(row=3, column=5)
Q_value_B2_E.grid(row=4, column=6)
Q_value_B2_S.grid(row=5, column=5)
Q_value_B3_W.grid(row=4, column=7)
Q_value_B3_N.grid(row=3, column=8)
Q_value_B3_E.grid(row=4, column=9)
Q_value_B3_S.grid(row=5, column=8)
Q_value_B4_W.grid(row=4, column=10)
Q_value_B4_N.grid(row=3, column=11)
Q_value_B4_E.grid(row=4, column=12)
Q_value_B4_S.grid(row=5, column=11)
Q_value_B5_W.grid(row=4, column=13)
Q_value_B5_N.grid(row=3, column=14)
Q_value_B5_E.grid(row=4, column=15)
Q_value_B5_S.grid(row=5, column=14)
B6_Wall.grid(row=4, column=17)
Q_value_B7.grid(row=4, column=20)

Q_value_C1.grid(row=7, column=2)
C2_Wall.grid(row=7, column=5)
Q_value_C3_W.grid(row=7, column=7)
Q_value_C3_N.grid(row=6, column=8)
Q_value_C3_E.grid(row=7, column=9)
Q_value_C3_S.grid(row=8, column=8)
Q_value_C4_W.grid(row=7, column=10)
Q_value_C4_N.grid(row=6, column=11)
Q_value_C4_E.grid(row=7, column=12)
Q_value_C4_S.grid(row=8, column=11)
C5_Wall.grid(row=7, column=14)
Q_value_C6_W.grid(row=7, column=16)
Q_value_C6_N.grid(row=6, column=17)
Q_value_C6_E.grid(row=7, column=18)
Q_value_C6_S.grid(row=8, column=17)
Q_value_C7.grid(row=7, column=20)

Q_value_D1.grid(row=10, column=2)
D2_Wall.grid(row=10, column=5)
Q_value_D3_W.grid(row=10, column=7)
Q_value_D3_N.grid(row=9, column=8)
Q_value_D3_E.grid(row=10, column=9)
Q_value_D3_S.grid(row=11, column=8)
Q_value_D4_goal.grid(row=10, column=11)
D5_Wall.grid(row=10, column=14)
Q_value_D6_W.grid(row=10, column=16)
Q_value_D6_N.grid(row=9, column=17)
Q_value_D6_E.grid(row=10, column=18)
Q_value_D6_S.grid(row=11, column=17)
Q_value_D7.grid(row=10, column=20)

Q_value_E1.grid(row=13, column=2)
Q_value_E2_W.grid(row=13, column=4)
Q_value_E2_N.grid(row=12, column=5)
Q_value_E2_E.grid(row=13, column=6)
Q_value_E2_S.grid(row=14, column=5)
Q_value_E3_W.grid(row=13, column=7)
Q_value_E3_N.grid(row=12, column=8)
Q_value_E3_E.grid(row=13, column=9)
Q_value_E3_S.grid(row=14, column=8)
Q_value_E4_W.grid(row=13, column=10)
Q_value_E4_N.grid(row=12, column=11)
Q_value_E4_E.grid(row=13, column=12)
Q_value_E4_S.grid(row=14, column=11)
Q_value_E5_W.grid(row=13, column=13)
Q_value_E5_N.grid(row=12, column=14)
Q_value_E5_E.grid(row=13, column=15)
Q_value_E5_S.grid(row=14, column=14)
Q_value_E6_W.grid(row=13, column=16)
Q_value_E6_N.grid(row=12, column=17)
Q_value_E6_E.grid(row=13, column=18)
Q_value_E6_S.grid(row=14, column=17)
Q_value_E7.grid(row=13, column=20)

Q_value_F1.grid(row=16, column=2)
Q_value_F2.grid(row=16, column=5)
Q_value_F3.grid(row=16, column=8)
Q_value_F4.grid(row=16, column=11)
Q_value_F5.grid(row=16, column=14)
Q_value_F6.grid(row=16, column=17)
Q_value_F7.grid(row=16, column=20)

n_value_maze = Tk()
n_value_maze.title("Windy Maze 'n' Values")

Total_visits_value_A1 = Label(n_value_maze, text=total_visits_table["A1"]["NORTH"], padx=10, pady=10)
Total_visits_value_A2 = Label(n_value_maze, text=total_visits_table["A2"]["NORTH"], padx=10, pady=10)
Total_visits_value_A3 = Label(n_value_maze, text=total_visits_table["A3"]["NORTH"], padx=10, pady=10)
Total_visits_value_A4 = Label(n_value_maze, text=total_visits_table["A4"]["NORTH"], padx=10, pady=10)
Total_visits_value_A5 = Label(n_value_maze, text=total_visits_table["A5"]["NORTH"], padx=10, pady=10)
Total_visits_value_A6 = Label(n_value_maze, text=total_visits_table["A6"]["NORTH"], padx=10, pady=10)
Total_visits_value_A7 = Label(n_value_maze, text=total_visits_table["A7"]["NORTH"], padx=10, pady=10)

Total_visits_value_B1 = Label(n_value_maze, text=total_visits_table["B1"]["NORTH"], padx=10, pady=10)
Total_visits_value_B2_W = Label(n_value_maze, text=total_visits_table["B2"]["WEST"], padx=10, pady=10)
Total_visits_value_B2_N = Label(n_value_maze, text=total_visits_table["B2"]["NORTH"], padx=10, pady=10)
Total_visits_value_B2_E = Label(n_value_maze, text=total_visits_table["B2"]["EAST"], padx=10, pady=10)
Total_visits_value_B2_S = Label(n_value_maze, text=total_visits_table["B2"]["SOUTH"], padx=10, pady=10)
Total_visits_value_B3_W = Label(n_value_maze, text=total_visits_table["B3"]["WEST"], padx=10, pady=10)
Total_visits_value_B3_N = Label(n_value_maze, text=total_visits_table["B3"]["NORTH"], padx=10, pady=10)
Total_visits_value_B3_E = Label(n_value_maze, text=total_visits_table["B3"]["EAST"], padx=10, pady=10)
Total_visits_value_B3_S = Label(n_value_maze, text=total_visits_table["B3"]["SOUTH"], padx=10, pady=10)
Total_visits_value_B4_W = Label(n_value_maze, text=total_visits_table["B4"]["WEST"], padx=10, pady=10)
Total_visits_value_B4_N = Label(n_value_maze, text=total_visits_table["B4"]["NORTH"], padx=10, pady=10)
Total_visits_value_B4_E = Label(n_value_maze, text=total_visits_table["B4"]["EAST"], padx=10, pady=10)
Total_visits_value_B4_S = Label(n_value_maze, text=total_visits_table["B4"]["SOUTH"], padx=10, pady=10)
Total_visits_value_B5_W = Label(n_value_maze, text=total_visits_table["B5"]["WEST"], padx=10, pady=10)
Total_visits_value_B5_N = Label(n_value_maze, text=total_visits_table["B5"]["NORTH"], padx=10, pady=10)
Total_visits_value_B5_E = Label(n_value_maze, text=total_visits_table["B5"]["EAST"], padx=10, pady=10)
Total_visits_value_B5_S = Label(n_value_maze, text=total_visits_table["B5"]["SOUTH"], padx=10, pady=10)
B6_Wall = Label(n_value_maze, text=initial_rewards_table["B6"], padx=10, pady=10)
Total_visits_value_B7 = Label(n_value_maze, text=total_visits_table["B7"]["NORTH"], padx=10, pady=10)

Total_visits_value_C1 = Label(n_value_maze, text=total_visits_table["C1"]["NORTH"], padx=10, pady=10)
C2_Wall = Label(n_value_maze, text=initial_rewards_table["C2"], padx=10, pady=10)
Total_visits_value_C3_W = Label(n_value_maze, text=total_visits_table["C3"]["WEST"], padx=10, pady=10)
Total_visits_value_C3_N = Label(n_value_maze, text=total_visits_table["C3"]["NORTH"], padx=10, pady=10)
Total_visits_value_C3_E = Label(n_value_maze, text=total_visits_table["C3"]["EAST"], padx=10, pady=10)
Total_visits_value_C3_S = Label(n_value_maze, text=total_visits_table["C3"]["SOUTH"], padx=10, pady=10)
Total_visits_value_C4_W = Label(n_value_maze, text=total_visits_table["C4"]["WEST"], padx=10, pady=10)
Total_visits_value_C4_N = Label(n_value_maze, text=total_visits_table["C4"]["NORTH"], padx=10, pady=10)
Total_visits_value_C4_E = Label(n_value_maze, text=total_visits_table["C4"]["EAST"], padx=10, pady=10)
Total_visits_value_C4_S = Label(n_value_maze, text=total_visits_table["C4"]["SOUTH"], padx=10, pady=10)
C5_Wall = Label(n_value_maze, text=initial_rewards_table["C5"], padx=10, pady=10)
Total_visits_value_C6_W = Label(n_value_maze, text=total_visits_table["C6"]["WEST"], padx=10, pady=10)
Total_visits_value_C6_N = Label(n_value_maze, text=total_visits_table["C6"]["NORTH"], padx=10, pady=10)
Total_visits_value_C6_E = Label(n_value_maze, text=total_visits_table["C6"]["EAST"], padx=10, pady=10)
Total_visits_value_C6_S = Label(n_value_maze, text=total_visits_table["C6"]["SOUTH"], padx=10, pady=10)
Total_visits_value_C7 = Label(n_value_maze, text=total_visits_table["C7"]["NORTH"], padx=10, pady=10)

Total_visits_value_D1 = Label(n_value_maze, text=total_visits_table["D1"]["NORTH"], padx=10, pady=10)
D2_Wall = Label(n_value_maze, text=initial_rewards_table["D2"], padx=10, pady=10)
Total_visits_value_D3_W = Label(n_value_maze, text=total_visits_table["D3"]["WEST"], padx=10, pady=10)
Total_visits_value_D3_N = Label(n_value_maze, text=total_visits_table["D3"]["NORTH"], padx=10, pady=10)
Total_visits_value_D3_E = Label(n_value_maze, text=total_visits_table["D3"]["EAST"], padx=10, pady=10)
Total_visits_value_D3_S = Label(n_value_maze, text=total_visits_table["D3"]["SOUTH"], padx=10, pady=10)
Total_visits_value_D4_goal = Label(n_value_maze, text=total_visits_table["D4"]["NORTH"], padx=10, pady=10)
D5_Wall = Label(n_value_maze, text=initial_rewards_table["D5"], padx=10, pady=10)
Total_visits_value_D6_W = Label(n_value_maze, text=total_visits_table["D6"]["WEST"], padx=10, pady=10)
Total_visits_value_D6_N = Label(n_value_maze, text=total_visits_table["D6"]["NORTH"], padx=10, pady=10)
Total_visits_value_D6_E = Label(n_value_maze, text=total_visits_table["D6"]["EAST"], padx=10, pady=10)
Total_visits_value_D6_S = Label(n_value_maze, text=total_visits_table["D6"]["SOUTH"], padx=10, pady=10)
Total_visits_value_D7 = Label(n_value_maze, text=total_visits_table["D7"]["NORTH"], padx=10, pady=10)

Total_visits_value_E1 = Label(n_value_maze, text=total_visits_table["E1"]["NORTH"], padx=10, pady=10)
Total_visits_value_E2_W = Label(n_value_maze, text=total_visits_table["E2"]["WEST"], padx=10, pady=10)
Total_visits_value_E2_N = Label(n_value_maze, text=total_visits_table["E2"]["NORTH"], padx=10, pady=10)
Total_visits_value_E2_E = Label(n_value_maze, text=total_visits_table["E2"]["EAST"], padx=10, pady=10)
Total_visits_value_E2_S = Label(n_value_maze, text=total_visits_table["E2"]["SOUTH"], padx=10, pady=10)
Total_visits_value_E3_W = Label(n_value_maze, text=total_visits_table["E3"]["WEST"], padx=10, pady=10)
Total_visits_value_E3_N = Label(n_value_maze, text=total_visits_table["E3"]["NORTH"], padx=10, pady=10)
Total_visits_value_E3_E = Label(n_value_maze, text=total_visits_table["E3"]["EAST"], padx=10, pady=10)
Total_visits_value_E3_S = Label(n_value_maze, text=total_visits_table["E3"]["SOUTH"], padx=10, pady=10)
Total_visits_value_E4_W = Label(n_value_maze, text=total_visits_table["E4"]["WEST"], padx=10, pady=10)
Total_visits_value_E4_N = Label(n_value_maze, text=total_visits_table["E4"]["NORTH"], padx=10, pady=10)
Total_visits_value_E4_E = Label(n_value_maze, text=total_visits_table["E4"]["EAST"], padx=10, pady=10)
Total_visits_value_E4_S = Label(n_value_maze, text=total_visits_table["E4"]["SOUTH"], padx=10, pady=10)
Total_visits_value_E5_W = Label(n_value_maze, text=total_visits_table["E5"]["WEST"], padx=10, pady=10)
Total_visits_value_E5_N = Label(n_value_maze, text=total_visits_table["E5"]["NORTH"], padx=10, pady=10)
Total_visits_value_E5_E = Label(n_value_maze, text=total_visits_table["E5"]["EAST"], padx=10, pady=10)
Total_visits_value_E5_S = Label(n_value_maze, text=total_visits_table["E5"]["SOUTH"], padx=10, pady=10)
Total_visits_value_E6_W = Label(n_value_maze, text=total_visits_table["E6"]["WEST"], padx=10, pady=10)
Total_visits_value_E6_N = Label(n_value_maze, text=total_visits_table["E6"]["NORTH"], padx=10, pady=10)
Total_visits_value_E6_E = Label(n_value_maze, text=total_visits_table["E6"]["EAST"], padx=10, pady=10)
Total_visits_value_E6_S = Label(n_value_maze, text=total_visits_table["E6"]["SOUTH"], padx=10, pady=10)
Total_visits_value_E7 = Label(n_value_maze, text=total_visits_table["E7"]["NORTH"], padx=10, pady=10)

Total_visits_value_F1 = Label(n_value_maze, text=total_visits_table["F1"]["NORTH"], padx=10, pady=10)
Total_visits_value_F2 = Label(n_value_maze, text=total_visits_table["F2"]["NORTH"], padx=10, pady=10)
Total_visits_value_F3 = Label(n_value_maze, text=total_visits_table["F3"]["NORTH"], padx=10, pady=10)
Total_visits_value_F4 = Label(n_value_maze, text=total_visits_table["F4"]["NORTH"], padx=10, pady=10)
Total_visits_value_F5 = Label(n_value_maze, text=total_visits_table["F5"]["NORTH"], padx=10, pady=10)
Total_visits_value_F6 = Label(n_value_maze, text=total_visits_table["F6"]["NORTH"], padx=10, pady=10)
Total_visits_value_F7 = Label(n_value_maze, text=total_visits_table["F7"]["NORTH"], padx=10, pady=10)

Total_visits_value_A1.grid(row=1, column=2)
Total_visits_value_A2.grid(row=1, column=5)
Total_visits_value_A3.grid(row=1, column=8)
Total_visits_value_A4.grid(row=1, column=11)
Total_visits_value_A5.grid(row=1, column=14)
Total_visits_value_A6.grid(row=1, column=17)
Total_visits_value_A7.grid(row=1, column=20)

Total_visits_value_B1.grid(row=4, column=2)
Total_visits_value_B2_W.grid(row=4, column=4)
Total_visits_value_B2_N.grid(row=3, column=5)
Total_visits_value_B2_E.grid(row=4, column=6)
Total_visits_value_B2_S.grid(row=5, column=5)
Total_visits_value_B3_W.grid(row=4, column=7)
Total_visits_value_B3_N.grid(row=3, column=8)
Total_visits_value_B3_E.grid(row=4, column=9)
Total_visits_value_B3_S.grid(row=5, column=8)
Total_visits_value_B4_W.grid(row=4, column=10)
Total_visits_value_B4_N.grid(row=3, column=11)
Total_visits_value_B4_E.grid(row=4, column=12)
Total_visits_value_B4_S.grid(row=5, column=11)
Total_visits_value_B5_W.grid(row=4, column=13)
Total_visits_value_B5_N.grid(row=3, column=14)
Total_visits_value_B5_E.grid(row=4, column=15)
Total_visits_value_B5_S.grid(row=5, column=14)
B6_Wall.grid(row=4, column=17)
Total_visits_value_B7.grid(row=4, column=20)

Total_visits_value_C1.grid(row=7, column=2)
C2_Wall.grid(row=7, column=5)
Total_visits_value_C3_W.grid(row=7, column=7)
Total_visits_value_C3_N.grid(row=6, column=8)
Total_visits_value_C3_E.grid(row=7, column=9)
Total_visits_value_C3_S.grid(row=8, column=8)
Total_visits_value_C4_W.grid(row=7, column=10)
Total_visits_value_C4_N.grid(row=6, column=11)
Total_visits_value_C4_E.grid(row=7, column=12)
Total_visits_value_C4_S.grid(row=8, column=11)
C5_Wall.grid(row=7, column=14)
Total_visits_value_C6_W.grid(row=7, column=16)
Total_visits_value_C6_N.grid(row=6, column=17)
Total_visits_value_C6_E.grid(row=7, column=18)
Total_visits_value_C6_S.grid(row=8, column=17)
Total_visits_value_C7.grid(row=7, column=20)

Total_visits_value_D1.grid(row=10, column=2)
D2_Wall.grid(row=10, column=5)
Total_visits_value_D3_W.grid(row=10, column=7)
Total_visits_value_D3_N.grid(row=9, column=8)
Total_visits_value_D3_E.grid(row=10, column=9)
Total_visits_value_D3_S.grid(row=11, column=8)
Total_visits_value_D4_goal.grid(row=10, column=11)
D5_Wall.grid(row=10, column=14)
Total_visits_value_D6_W.grid(row=10, column=16)
Total_visits_value_D6_N.grid(row=9, column=17)
Total_visits_value_D6_E.grid(row=10, column=18)
Total_visits_value_D6_S.grid(row=11, column=17)
Total_visits_value_D7.grid(row=10, column=20)

Total_visits_value_E1.grid(row=13, column=2)
Total_visits_value_E2_W.grid(row=13, column=4)
Total_visits_value_E2_N.grid(row=12, column=5)
Total_visits_value_E2_E.grid(row=13, column=6)
Total_visits_value_E2_S.grid(row=14, column=5)
Total_visits_value_E3_W.grid(row=13, column=7)
Total_visits_value_E3_N.grid(row=12, column=8)
Total_visits_value_E3_E.grid(row=13, column=9)
Total_visits_value_E3_S.grid(row=14, column=8)
Total_visits_value_E4_W.grid(row=13, column=10)
Total_visits_value_E4_N.grid(row=12, column=11)
Total_visits_value_E4_E.grid(row=13, column=12)
Total_visits_value_E4_S.grid(row=14, column=11)
Total_visits_value_E5_W.grid(row=13, column=13)
Total_visits_value_E5_N.grid(row=12, column=14)
Total_visits_value_E5_E.grid(row=13, column=15)
Total_visits_value_E5_S.grid(row=14, column=14)
Total_visits_value_E6_W.grid(row=13, column=16)
Total_visits_value_E6_N.grid(row=12, column=17)
Total_visits_value_E6_E.grid(row=13, column=18)
Total_visits_value_E6_S.grid(row=14, column=17)
Total_visits_value_E7.grid(row=13, column=20)

Total_visits_value_F1.grid(row=16, column=2)
Total_visits_value_F2.grid(row=16, column=5)
Total_visits_value_F3.grid(row=16, column=8)
Total_visits_value_F4.grid(row=16, column=11)
Total_visits_value_F5.grid(row=16, column=14)
Total_visits_value_F6.grid(row=16, column=17)
Total_visits_value_F7.grid(row=16, column=20)


visual_maze.mainloop()
n_value_maze.mainloop()
