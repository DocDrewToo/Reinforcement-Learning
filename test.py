import unittest
import main

class MainTests(unittest.TestCase):

    def test_random_direction_matches_a_defined_direction(self):
        message = "Verify a randomily generated direction is a valid one"
        expected_directions_string = "".join(main.directions)
        random_direction = main.get_random_direction()

        self.assertIn(random_direction, expected_directions_string, message)


    def test_ramdomily_entering_room_is_valid_room(self):
        message = "Initial random entry into 'maze' is a valid room"
        list_of_valid_rooms_string = "".join(main.maze_positions)
        starting_position = main.starting_position(main.maze_positions)     

        self.assertIn(starting_position, list_of_valid_rooms_string, message)


if __name__ == '__main__':
    unittest.main()
