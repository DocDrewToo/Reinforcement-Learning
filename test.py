import unittest
import main


class MainTests(unittest.TestCase):

    def test_get_max_q_value(self):
        position_in_maze = "B2"
        main.q_value_table = {"B2":
                                  {"NORTH": 5, "SOUTH": 1, "EAST": 1, "WEST": 1}
                              }
        expected_max_q_value = 5
        actual_max_q_value = main.get_max_q_value(position_in_maze)

        self.assertEqual(expected_max_q_value, actual_max_q_value)

    def test_next_direction_is_max_value_zero_epsilon(self):
        main.epsilon = 0
        expected_direction = "NORTH"
        main.q_value_table = {"B2":
                                  {"NORTH": 5, "SOUTH": 1, "EAST": 1, "WEST": 1}
                              }
        calculated_direction = main.best_direction_to_move("B2")

        self.assertEqual(expected_direction, calculated_direction)

    def test_ramdom_room_is_valid_room(self):
        message = "Initial random entry into 'maze' is a valid room"
        list_of_valid_rooms_string = "".join(main.valid_starting_positions)
        starting_position = main.starting_position()

        self.assertIn(starting_position, list_of_valid_rooms_string, message)

    def test_calculated_q_value(self):
        current_position = "B2"
        current_direction = "EAST"
        future_position = "B3"
        main.total_visits_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 9, "WEST": 0}
        main.q_value_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 5, "WEST": 0}
        main.q_value_table["B3"] = {"NORTH": 2, "SOUTH": 50, "EAST": 5, "WEST": 2}

        expected_q_value = 8.8
        actual_q_value = main.calculate_q_value(current_position,
                                                current_direction, future_position)

        self.assertEqual(expected_q_value, actual_q_value)

    def test_calculated_q_value_when_hitting_a_wall(self):
        current_position = "B2"
        current_direction = "EAST"
        future_position = "B2"
        main.total_visits_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 1, "WEST": 0}
        main.q_value_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": -2, "WEST": 0}

        expected_q_value = -2
        actual_q_value = main.calculate_q_value(current_position,
                                                current_direction, future_position)

        self.assertEqual(expected_q_value, actual_q_value)

    def test_c3_heading_north_with_zero_drift_is_b3(self):
        position = "C3"
        direction = "NORTH"
        expected_next_maze_position = "B3"
        main.chance_to_drift_right = 0
        main.chance_to_drift_left = 0

        actual_next_maze_position = main.get_next_position(position, direction)
        self.assertEqual(expected_next_maze_position, actual_next_maze_position)

    def test_c3_heading_east_with_zero_drift_is_c4(self):
        position = "C3"
        direction = "EAST"
        expected_next_maze_position = "C4"
        main.chance_to_drift_right = 0
        main.chance_to_drift_left = 0

        actual_next_maze_position = main.get_next_position(position, direction)
        self.assertEqual(expected_next_maze_position, actual_next_maze_position)

    def test_c3_heading_south_with_zero_drift_is_d3(self):
        position = "C3"
        direction = "SOUTH"
        expected_next_maze_position = "D3"
        main.chance_to_drift_right = 0
        main.chance_to_drift_left = 0
        
        actual_next_maze_position = main.get_next_position(position, direction)
        self.assertEqual(expected_next_maze_position, actual_next_maze_position)

    def test_c4_heading_west_with_zero_drift_is_c3(self):
        position = "C4"
        direction = "WEST"
        expected_next_maze_position = "C3"
        main.chance_to_drift_right = 0
        main.chance_to_drift_left = 0
        
        actual_next_maze_position = main.get_next_position(position, direction)
        self.assertEqual(expected_next_maze_position, actual_next_maze_position)

    def test_c3_heading_west_with_zero_drift_hits_wall_is_c3(self):
        position = "C3"
        direction = "WEST"
        expected_next_maze_position = "C3"
        main.chance_to_drift_right = 0
        main.chance_to_drift_left = 0
        
        actual_next_maze_position = main.get_next_position(position, direction)
        self.assertEqual(expected_next_maze_position, actual_next_maze_position)

    def test_heading_north_to_the_left_is_west(self):
        direction = "NORTH"
        expected_direction_to_the_left = "WEST"

        actual_direction_to_the_left = main.headed_this_way_to_the_left_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_south_to_the_left_is_east(self):
        direction = "SOUTH"
        expected_direction_to_the_left = "EAST"

        actual_direction_to_the_left = main.headed_this_way_to_the_left_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_east_to_the_left_is_north(self):
        direction = "EAST"
        expected_direction_to_the_left = "NORTH"

        actual_direction_to_the_left = main.headed_this_way_to_the_left_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_west_to_the_left_is_south(self):
        direction = "WEST"
        expected_direction_to_the_left = "SOUTH"

        actual_direction_to_the_left = main.headed_this_way_to_the_left_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_north_to_the_right_is_east(self):
        direction = "NORTH"
        expected_direction_to_the_left = "EAST"

        actual_direction_to_the_left = main.headed_this_way_to_the_right_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_south_to_the_right_is_west(self):
        direction = "SOUTH"
        expected_direction_to_the_left = "WEST"

        actual_direction_to_the_left = main.headed_this_way_to_the_right_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_east_to_the_right_is_south(self):
        direction = "EAST"
        expected_direction_to_the_left = "SOUTH"

        actual_direction_to_the_left = main.headed_this_way_to_the_right_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_heading_west_to_the_right_is_north(self):
        direction = "WEST"
        expected_direction_to_the_left = "NORTH"

        actual_direction_to_the_left = main.headed_this_way_to_the_right_is(direction)
        self.assertEqual(expected_direction_to_the_left, actual_direction_to_the_left)

    def test_update_q_value_correctly_override_previous_value(self):
        main.q_value_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 5, "WEST": 0}

        main.update_q_value("B2", "EAST", 10)
        expected_q_value = 10
        actual_q_value = main.q_value_table["B2"].get("EAST")

        self.assertEqual(expected_q_value, actual_q_value)

    def test_update_total_visits_correctly_override_previous_value_by_1(self):
        main.total_visits_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 5, "WEST": 0}

        main.update_total_times_this_direction("B2", "EAST")
        expected_q_value = 6
        actual_q_value = main.total_visits_table["B2"].get("EAST")

        self.assertEqual(expected_q_value, actual_q_value)

    def test_preloading_of_total_visits_table(self):
        expected_total_visits_table = {
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
        actual_total_visits_table = main.preload_total_visits_table()

        self.assertEqual(expected_total_visits_table, actual_total_visits_table)

    def test_preloading_of_q_value_table(self):
        expected_q_value_table = {
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

        actual_q_value_table = main.preload_q_value_table()
        self.assertEqual(expected_q_value_table, actual_q_value_table)


if __name__ == '__main__':
    unittest.main()
