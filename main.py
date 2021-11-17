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

    # print(q_value_table["A2"]["NORTH"])
    # print("___________________")
    # print(total_visits_table)

Row1 = list(initial_rewards_table.values())[0:7]
Row2 = list(initial_rewards_table.values())[7:14]
Row3 = list(initial_rewards_table.values())[14:21]
Row4 = list(initial_rewards_table.values())[21:28]
Row5 = list(initial_rewards_table.values())[28:35]
Row6 = list(initial_rewards_table.values())[35:42]

visual_maze = Tk()
visual_maze.title("Windy Maze")

mylabel1 = Label(visual_maze, text=directions, padx=20, pady=20)

mylabel2 = Label(visual_maze, text=Row1[1], padx=20, pady=20)
mylabel3 = Label(visual_maze, text=Row1[2], padx=20, pady=20)
mylabel4 = Label(visual_maze, text=Row1[3], padx=20, pady=20)
mylabel5 = Label(visual_maze, text=Row1[4], padx=20, pady=20)
mylabel6 = Label(visual_maze, text=Row1[5], padx=20, pady=20)
mylabel7 = Label(visual_maze, text=Row1[6], padx=20, pady=20)

mylabel8 = Label(visual_maze, text=Row2[0], padx=20, pady=20)
mylabel9 = Label(visual_maze, text=Row2[1], padx=20, pady=20)
mylabel10 = Label(visual_maze, text=Row2[2], padx=20, pady=20)
mylabel11 = Label(visual_maze, text=Row2[3], padx=20, pady=20)
mylabel12 = Label(visual_maze, text=Row2[4], padx=20, pady=20)
mylabel13 = Label(visual_maze, text=Row2[5], padx=20, pady=20)
mylabel14 = Label(visual_maze, text=Row2[6], padx=20, pady=20)

mylabel15 = Label(visual_maze, text=Row3[0], padx=20, pady=20)
mylabel16 = Label(visual_maze, text=Row3[1], padx=20, pady=20)
mylabel17 = Label(visual_maze, text=Row3[2], padx=20, pady=20)
mylabel18 = Label(visual_maze, text=Row3[3], padx=20, pady=20)
mylabel19 = Label(visual_maze, text=Row3[4], padx=20, pady=20)
mylabel20 = Label(visual_maze, text=Row3[5], padx=20, pady=20)
mylabel21 = Label(visual_maze, text=Row3[6], padx=20, pady=20)

mylabel22 = Label(visual_maze, text=Row4[0], padx=20, pady=20)
mylabel23 = Label(visual_maze, text=Row4[1], padx=20, pady=20)
mylabel24 = Label(visual_maze, text=Row4[2], padx=20, pady=20)
mylabel25 = Label(visual_maze, text=Row4[3], padx=20, pady=20)
mylabel26 = Label(visual_maze, text=Row4[4], padx=20, pady=20)
mylabel27 = Label(visual_maze, text=Row4[5], padx=20, pady=20)
mylabel28 = Label(visual_maze, text=Row4[6], padx=20, pady=20)

mylabel29 = Label(visual_maze, text=Row5[0], padx=20, pady=20)
mylabel30 = Label(visual_maze, text=Row5[1], padx=20, pady=20)
mylabel31 = Label(visual_maze, text=Row5[2], padx=20, pady=20)
mylabel32 = Label(visual_maze, text=Row5[3], padx=20, pady=20)
mylabel33 = Label(visual_maze, text=Row5[4], padx=20, pady=20)
mylabel34 = Label(visual_maze, text=Row5[5], padx=20, pady=20)
mylabel35 = Label(visual_maze, text=Row5[6], padx=20, pady=20)

mylabel36 = Label(visual_maze, text=Row6[0], padx=20, pady=20)
mylabel37 = Label(visual_maze, text=Row6[1], padx=20, pady=20)
mylabel38 = Label(visual_maze, text=Row6[2], padx=20, pady=20)
mylabel39 = Label(visual_maze, text=Row6[3], padx=20, pady=20)
mylabel40 = Label(visual_maze, text=Row6[4], padx=20, pady=20)
mylabel41 = Label(visual_maze, text=Row6[5], padx=20, pady=20)
mylabel42 = Label(visual_maze, text=Row6[6], padx=20, pady=20)

mylabel1.grid(row=0, column=0)
mylabel2.grid(row=0, column=1)
mylabel3.grid(row=0, column=2)
mylabel4.grid(row=0, column=3)
mylabel5.grid(row=0, column=4)
mylabel6.grid(row=0, column=5)
mylabel7.grid(row=0, column=6)

mylabel8.grid(row=1, column=0)
mylabel9.grid(row=1, column=1)
mylabel10.grid(row=1, column=2)
mylabel11.grid(row=1, column=3)
mylabel12.grid(row=1, column=4)
mylabel13.grid(row=1, column=5)
mylabel14.grid(row=1, column=6)

mylabel15.grid(row=2, column=0)
mylabel16.grid(row=2, column=1)
mylabel17.grid(row=2, column=2)
mylabel18.grid(row=2, column=3)
mylabel19.grid(row=2, column=4)
mylabel20.grid(row=2, column=5)
mylabel21.grid(row=2, column=6)

mylabel22.grid(row=3, column=0)
mylabel23.grid(row=3, column=1)
mylabel24.grid(row=3, column=2)
mylabel25.grid(row=3, column=3)
mylabel26.grid(row=3, column=4)
mylabel27.grid(row=3, column=5)
mylabel28.grid(row=3, column=6)

mylabel29.grid(row=4, column=0)
mylabel30.grid(row=4, column=1)
mylabel31.grid(row=4, column=2)
mylabel32.grid(row=4, column=3)
mylabel33.grid(row=4, column=4)
mylabel34.grid(row=4, column=5)
mylabel35.grid(row=4, column=6)

mylabel36.grid(row=5, column=0)
mylabel37.grid(row=5, column=1)
mylabel38.grid(row=5, column=2)
mylabel39.grid(row=5, column=3)
mylabel40.grid(row=5, column=4)
mylabel41.grid(row=5, column=5)
mylabel42.grid(row=5, column=6)

visual_maze.mainloop()
