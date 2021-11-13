import random


gamma = 0.9
epsilon = 0.1
total_visits_table = {}

q_value_table = {}

valid_starting_positions = ("B2","B3","B4","B5",
                            "C3","C4","C6",
                            "D3","D6",
                            "E2","E3","E4","E5","E6",
                            )
intial_rewards_table = {
  "A1":-50,"A2":-50,"A3":-50,"A4":-50,"A5":-50,"A6":-50,"A7":-50,
  "B1":-50,"B2":0,"B3":0,"B4":0,"B5":0,"B6":"WALL","B7":-50,
  "C1":-50,"C2":"WALL","C3":0,"C4":0,"C5":"WALL","C6":0,"C7":-50,
  "D1":-50,"D2":"WALL","D3":0,"D4":100,"D5":"WALL","D6":0,"D7":-50,
  "E1":-50,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":-50,
  "F1":-50,"F2":-50,"F3":-50,"F4":-50,"F5":-50,"F6":-50,"F7":-50,
}

reward_for_move = {
    "NORTH":-3,
    "SOUTH":-1,
    "EAST":-2,
    "WEST":-2
}

directions = ("NORTH",
              "SOUTH",
              "EAST",
              "WEST")


def starting_position():
    return random.choice(valid_starting_positions)

  
def best_direction_to_move(position):
    best_direction = ""
    #Use max q for best direction, unless hit by randomness introduced by epsilon
    if ( random.random() <= epsilon) :
        best_direction = random.choice(directions)
        print("Random direction triggered! for Position: ", position, 
        "Now heading ", best_direction)
        return best_direction

    max_q_value = get_max_q_value(position)

    list_of_directions_for_position = list(q_value_table.get(position).keys())
    list_of_q_values_for_position = list(q_value_table.get(position).values())
    index_of_max_q_value = list_of_q_values_for_position.index(max_q_value)

    best_direction = list_of_directions_for_position[index_of_max_q_value]

    return best_direction

def get_max_q_value(position):
    all_directions_at_position = q_value_table.get(position)
    
    #TODO itterate through directions
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
         ( current_action_reward + gamma * \
         max_future_q_value - current_state_q )
    return gamma_probability

if __name__ == "__main__":
    print("Hello")