import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    """
    Integration tests for the Flask application.
    """

    def setUp(self):
        """
        Set up the test client.
        """
        self.app = app.test_client()
        self.app.testing = True

    def perform_invalid_input_test(self, endpoint, input_data, expected_error_message):
        """
        Helper function to test invalid inputs for the specified endpoint.
        """
        response = self.app.post(endpoint, data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(expected_error_message.encode(), response.data)

    def test_home_page(self):
        """
        Test that the home page loads correctly.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Auto Driving Car Simulator', response.data)

    # Part 1 Tests

    def test_simulate_part1_valid_input(self):
        """
        Test the /simulate_part1 endpoint with valid input.
        """
        input_data = '10 10\n1 2 N\nFFRFFFRRLF'
        response = self.app.post('/simulate_part1', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '4 3 S')

    def test_simulate_part1_invalid_field_dimensions(self):
        """
        Test the /simulate_part1 endpoint with invalid field dimensions.
        """
        input_data = '10 A\n1 2 N\nFFRFFFRRLF'
        expected_error_message = 'Error: Field dimensions must be integers.'
        self.perform_invalid_input_test('/simulate_part1', input_data, expected_error_message)

    def test_simulate_part1_invalid_position(self):
        """
        Test the /simulate_part1 endpoint with invalid initial position.
        """
        input_data = '10 10\nA 2 N\nFFRFFFRRLF'
        expected_error_message = 'Error: Initial position must be integers.'
        self.perform_invalid_input_test('/simulate_part1', input_data, expected_error_message)

    def test_simulate_part1_invalid_direction(self):
        """
        Test the /simulate_part1 endpoint with invalid initial direction.
        """
        input_data = '10 10\n1 2 X\nFFRFFFRRLF'
        expected_error_message = "Error: Initial direction must be one of 'N', 'E', 'S', or 'W'."
        self.perform_invalid_input_test('/simulate_part1', input_data, expected_error_message)

    def test_simulate_part1_invalid_commands(self):
        """
        Test the /simulate_part1 endpoint with invalid commands.
        """
        input_data = '10 10\n1 2 N\nFFRXFFYFRRLZ'
        expected_error_message = "Error: Commands must be a sequence of 'R', 'L', and 'F' only."
        self.perform_invalid_input_test('/simulate_part1', input_data, expected_error_message)

    def test_boundary_conditions_part1(self):
        """
        Test the /simulate_part1 endpoint for boundary conditions.
        """
        boundary_test_cases = [
            ('10 10\n0 0 S\nFFFF\n', '0 0 S'),  # Bottom boundary
            ('10 10\n0 0 W\nFFFF\n', '0 0 W'),  # Left boundary
            ('10 10\n9 9 N\nFFFF\n', '9 9 N'),  # Top boundary
            ('10 10\n9 9 E\nFFFF\n', '9 9 E'),  # Right boundary
        ]

        for input_data, expected_output in boundary_test_cases:
            response = self.app.post('/simulate_part1', data={'input': input_data})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), expected_output)

    # Part 2 Tests

    def test_simulate_part2_valid_input(self):
        """
        Test the /simulate_part2 endpoint with valid input.
        """
        input_data = '10 10\n\nA\n1 2 N\nFFRFFFFRRL\n\nB\n7 8 W\nFFLFFFFFFF'
        response = self.app.post('/simulate_part2', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'A B\n5 4\n7')

    def test_simulate_part2_no_collision(self):
        """
        Test the /simulate_part2 endpoint when no collision occurs.
        """
        input_data = '10 10\n\nA\n1 2 N\nFFF\n\nB\n7 8 W\nFFFL'
        response = self.app.post('/simulate_part2', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'no collision')

    def test_simulate_part2_invalid_input_format(self):
        """
        Test the /simulate_part2 endpoint with invalid input format.
        """
        input_data = '10 10\nA\n1 2 N\nFFRFFFFRRL'  # Missing second car
        expected_error_message = 'Error: Invalid input format. Please provide field size and details for each car.'
        self.perform_invalid_input_test('/simulate_part2', input_data, expected_error_message)

    def test_simulate_part2_invalid_direction(self):
        """
        Test the /simulate_part2 endpoint with an invalid direction for a car.
        """
        input_data = '10 10\n\nA\n1 2 X\nFFRFFFFRRL\n\nB\n7 8 W\nFFLFFFFFFF'
        expected_error_message = "Error: Invalid direction for car A. Must be one of 'N', 'E', 'S', 'W'."
        self.perform_invalid_input_test('/simulate_part2', input_data, expected_error_message)

    def test_simulate_part2_invalid_commands(self):
        """
        Test the /simulate_part2 endpoint with invalid commands for a car.
        """
        input_data = '10 10\n\nA\n1 2 N\nFFRXFFYFRRLZ\n\nB\n7 8 W\nFFLFFFFFFF'
        expected_error_message = "Error: Invalid commands for car A. Must be 'R', 'L', 'F' only."
        self.perform_invalid_input_test('/simulate_part2', input_data, expected_error_message)

if __name__ == '__main__':
    unittest.main()