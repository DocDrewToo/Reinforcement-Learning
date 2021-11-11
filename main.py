import random

total_visits_table = {}

q_value_table = {}
maze_positions = ("A1","A2","A3","A4","A5","A6","A7",
                  "B1","B2","B3","B4","B5","B6","B7",
                  "C1","C2","C3","C4","C5","C6","C7",
                  "D1","D2","D3","D4","D5","D6","D7",
                  "E1","E2","E3","E4","E5","E6","E7",
                  "F1","F2","F3","F4","F5","F6","F7")


reward_table = {
  "A1":-50,"A2":-50,"A3":-50,"A4":-50,"A5":-50,"A6":-50,"A7":-50,
  "B1":-50,"B2":0,"B3":0,"B4":0,"B5":0,"B6":"WALL","B7":-50,
  "C1":-50,"C2":"WALL","C3":0,"C4":0,"C5":"WALL","C6":0,"C7":-50,
  "D1":-50,"D2":"WALL","D3":0,"D4":100,"D5":"WALL","D6":0,"D7":-50,
  "E1":-50,"E2":0,"E3":0,"E4":0,"E5":0,"E6":0,"E7":-50,
  "F1":-50,"F2":-50,"F3":-50,"F4":-50,"F5":-50,"F6":-50,"F7":-50,
}

cost_to_move = {
    "NORTH":-3,
    "SOUTH":-1,
    "EAST":-2,
    "WEST":-2
}

reward_to_move = {
    "NORTH":3,
    "SOUTH":1,
    "EAST":2,
    "WEST":2
}

directions = ["NORTH",
              "SOUTH",
              "EAST",
              "WEST"]

def starting_position(maze):
    return random.choice(maze)


def get_random_direction():
    return random.choice(directions)

  
if __name__ == "__main__":
    for x in range(1,10):
        print(x, get_random_direction())
