import unittest
from src.car import Car
from src.field import Field

class TestCar(unittest.TestCase):
    """
    Unit tests for the Car class functionality.
    """

    def test_initial_position(self):
        """
        Test the initial position and direction of the car.
        """
        car = Car(1, 2, 'N')
        self.assertEqual(car.get_position(), "1 2 N")

    def test_rotate_left(self):
        """
        Test the car's rotation to the left.
        """
        car = Car(1, 2, 'N')
        car.rotate_left()
        self.assertEqual(car.get_position(), "1 2 W")
        car.rotate_left()
        self.assertEqual(car.get_position(), "1 2 S")
        car.rotate_left()
        self.assertEqual(car.get_position(), "1 2 E")
        car.rotate_left()
        self.assertEqual(car.get_position(), "1 2 N")

    def test_rotate_right(self):
        """
        Test the car's rotation to the right.
        """
        car = Car(1, 2, 'N')
        car.rotate_right()
        self.assertEqual(car.get_position(), "1 2 E")
        car.rotate_right()
        self.assertEqual(car.get_position(), "1 2 S")
        car.rotate_right()
        self.assertEqual(car.get_position(), "1 2 W")
        car.rotate_right()
        self.assertEqual(car.get_position(), "1 2 N")

    def test_move_forward(self):
        """
        Test the car's movement forward within field boundaries.
        """
        field = Field(10, 10)
        car = Car(1, 2, 'N')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "1 3 N")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "2 3 E")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "2 2 S")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "1 2 W")

    def test_execute_commands(self):
        """
        Test the car's execution of a sequence of commands.
        """
        field = Field(10, 10)
        car = Car(1, 2, 'N')
        commands = "FFRFFFRRLF"
        car.execute_commands(commands, field)
        self.assertEqual(car.get_position(), "4 3 S")

    def test_invalid_commands(self):
        """
        Test the car's behavior with invalid commands.
        Car should ignore invalid commands.
        """
        field = Field(10, 10)
        car = Car(1, 2, 'N')
        commands = "FFRXFFYFRRLZ"
        car.execute_commands(commands, field)
        self.assertEqual(car.get_position(), "4 4 S")

    def test_invalid_initialization(self):
        """
        Test the car initialization with invalid parameters.
        """
        with self.assertRaises(ValueError):
            Car(-1, 2, 'N')
        with self.assertRaises(ValueError):
            Car(1, -2, 'N')
        with self.assertRaises(ValueError):
            Car(1, 2, 'X')  # Invalid direction

if __name__ == '__main__':
    unittest.main()
