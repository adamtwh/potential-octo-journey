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

    def test_home_page(self):
        """
        Test that the home page loads correctly.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Auto Driving Car Simulator', response.data)

    def test_simulate_valid_input(self):
        """
        Test the simulate endpoint with valid input.
        """
        input_data = '10 10\n1 2 N\nFFRFFFRRLF'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '4 3 S')

    def test_simulate_invalid_lines(self):
        """
        Test the simulate endpoint with invalid number of input lines.
        """
        input_data = '10 10\n1 2 N'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: Please provide exactly 3 lines of input.', response.data)

    def test_simulate_invalid_field_dimensions(self):
        """
        Test the simulate endpoint with invalid field dimensions.
        """
        input_data = '10 A\n1 2 N\nFFRFFFRRLF'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: Field dimensions must be integers.', response.data)

    def test_simulate_invalid_position(self):
        """
        Test the simulate endpoint with invalid initial position.
        """
        input_data = '10 10\nA 2 N\nFFRFFFRRLF'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Error: Initial position must be integers.', response.data)

    def test_simulate_invalid_direction(self):
        """
        Test the simulate endpoint with invalid initial direction.
        """
        input_data = '10 10\n1 2 X\nFFRFFFRRLF'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Error: Initial direction must be one of 'N', 'E', 'S', or 'W'.", response.data)

    def test_simulate_invalid_commands(self):
        """
        Test the simulate endpoint with invalid commands.
        """
        input_data = '10 10\n1 2 N\nFFRXFFYFRRLZ'
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Error: Commands must be a sequence of 'R', 'L', and 'F' only.", response.data)

    def test_boundary_conditions(self):
        """
        Test the car's behavior at the field boundaries.
        """
        input_data = '10 10\n0 0 S\nFFFF\n'  # Car should not move as it is already at the bottom boundary.
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '0 0 S')

        input_data = '10 10\n0 0 W\nFFFF\n'  # Car should not move as it is already at the left boundary.
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '0 0 W')

        input_data = '10 10\n9 9 N\nFFFF\n'  # Car should not move as it is already at the top boundary.
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '9 9 N')

        input_data = '10 10\n9 9 E\nFFFF\n'  # Car should not move as it is already at the right boundary.
        response = self.app.post('/simulate', data={'input': input_data})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '9 9 E')

if __name__ == '__main__':
    unittest.main()
