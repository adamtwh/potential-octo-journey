class Field:
    """
    Represents a rectangular field for the car to move within.
    """

    def __init__(self, width, height):
        """
        Initializes the field with the given width and height.
        Raises ValueError if width or height is negative or not an integer.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Width and height must be integers.")
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height


class Car:
    """
    Represents the car with position and direction.
    """
    directions = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, direction):
        """
        Initializes the car's position and direction.
        Raises ValueError if coordinates are negative, not integers, or direction is invalid.
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("Coordinates must be integers.")
        if x < 0 or y < 0:
            raise ValueError("Coordinates must be non-negative.")
        if direction not in self.directions:
            raise ValueError("Invalid direction. Must be 'N', 'E', 'S', or 'W'.")
        self.x = x
        self.y = y
        self.direction = direction

    def get_position(self):
        """
        Returns the current position and direction of the car.
        """
        return f"{self.x} {self.y} {self.direction}"

    def rotate_left(self):
        """
        Rotates the car 90 degrees to the left.
        """
        self.direction = self.directions[(self.directions.index(self.direction) - 1) % 4]

    def rotate_right(self):
        """
        Rotates the car 90 degrees to the right.
        """
        self.direction = self.directions[(self.directions.index(self.direction) + 1) % 4]

    def move_forward(self, field):
        """
        Moves the car forward by one grid point, if within field boundaries.
        """
        if self.direction == 'N' and self.y < field.height - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < field.width - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def execute_commands(self, commands, field):
        """
        Executes a sequence of commands to control the car.
        Ignores any invalid commands.
        """
        for command in commands:
            if command == 'L':
                self.rotate_left()
            elif command == 'R':
                self.rotate_right()
            elif command == 'F':
                self.move_forward(field)
