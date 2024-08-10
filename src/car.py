class Car:
    """
    Represents the car with position and direction.
    """

    # Directions in clockwise order: North, East, South, West
    directions = ['N', 'E', 'S', 'W']
    direction_delta = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)
    }

    def __init__(self, x, y, direction, identifier=None):
        """
        Initializes the car's position, direction, and optionally, an identifier.
        Raises ValueError if coordinates are negative or direction is invalid.
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
        self.identifier = identifier  # Optional identifier for the car

    def get_position(self):
        """
        Returns the current position and direction of the car as a string.
        """
        return f"{self.x} {self.y} {self.direction}"

    def get_position_with_id(self):
        """
        Returns the current position, direction, and identifier of the car as a string.
        """
        if self.identifier:
            return f"{self.identifier} {self.x} {self.y} {self.direction}"
        return self.get_position()

    def rotate_left(self):
        """
        Rotates the car 90 degrees to the left.
        """
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index - 1) % 4]

    def rotate_right(self):
        """
        Rotates the car 90 degrees to the right.
        """
        current_index = self.directions.index(self.direction)
        self.direction = self.directions[(current_index + 1) % 4]

    def move_forward(self, field):
        """
        Moves the car forward by one grid point, if within field boundaries.
        Delegates boundary checking to the Field class.
        """
        delta_x, delta_y = self.direction_delta[self.direction]
        potential_x, potential_y = self.x + delta_x, self.y + delta_y
        
        if field.is_within_bounds(potential_x, potential_y):
            self.x, self.y = potential_x, potential_y

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