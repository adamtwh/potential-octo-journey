import unittest
from src.car import Car
from src.field import Field

class TestField(unittest.TestCase):
    """
    Unit tests for the Field class functionality.
    """

    def test_field_initialization(self):
        """
        Test the field initialization with valid parameters.
        """
        field = Field(10, 10)
        self.assertEqual(field.width, 10)
        self.assertEqual(field.height, 10)

    def test_movement_within_bounds(self):
        """
        Test the car's movement within the field boundaries.
        """
        field = Field(10, 10)
        car = Car(5, 5, 'N')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "5 6 N")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "6 6 E")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "6 5 S")
        car.rotate_right()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "5 5 W")

    def test_boundary_conditions(self):
        """
        Test the car's behavior at the field boundaries.
        Car should not move beyond boundaries.
        """
        field = Field(10, 10)
        
        # Test lower boundary
        car = Car(0, 0, 'S')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "0 0 S")
        
        car = Car(0, 0, 'W')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "0 0 W")
        
        # Test upper boundary
        car = Car(9, 9, 'N')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "9 9 N")
        
        car = Car(9, 9, 'E')
        car.move_forward(field)
        self.assertEqual(car.get_position(), "9 9 E")

    def test_smallest_field(self):
        """
        Test the field behavior when it is the smallest possible size (1x1).
        """
        field = Field(1, 1)
        car = Car(0, 0, 'N')
        
        car.move_forward(field)
        self.assertEqual(car.get_position(), "0 0 N")
        
        car.rotate_left()
        car.move_forward(field)
        self.assertEqual(car.get_position(), "0 0 W")

    def test_invalid_initialization(self):
        """
        Test the field initialization with invalid parameters.
        """
        with self.assertRaises(ValueError):
            Field(-1, 10)
        with self.assertRaises(ValueError):
            Field(10, -1)

    def test_field_with_multiple_cars(self):
        """
        Test the field's ability to manage multiple cars and detect collisions.
        """

        field = Field(10, 10)
        car_a = Car(1, 2, 'N', 'A')
        car_b = Car(7, 8, 'W', 'B')
        
        commands_a = "FFRFFFFRRL"
        commands_b = "FFLFFFFFFF"
        
        result = field.simulate_multiple_cars([
            (car_a, commands_a),
            (car_b, commands_b)
        ])
        
        # Expected output
        expected_output = "A B\n5 4\n7"
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()