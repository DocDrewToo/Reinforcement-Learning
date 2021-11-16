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
        future_direction = "SOUTH"
        main.total_visits_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 9, "WEST": 0}
        main.q_value_table["B2"] = {"NORTH": 0, "SOUTH": 0, "EAST": 5, "WEST": 0}
        main.q_value_table["B3"] = {"NORTH": 2, "SOUTH": 50, "EAST": 5, "WEST": 2}

        expected_q_value = 8.8
        actual_q_value = main.calculate_q_value(current_position,
                                                current_direction, future_position, future_direction)

        self.assertEqual(expected_q_value, actual_q_value)


if __name__ == '__main__':
    unittest.main()
