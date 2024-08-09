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

    def is_within_bounds(self, x, y):
        """
        Checks if the given (x, y) position is within the field boundaries.
        """
        return 0 <= x < self.width and 0 <= y < self.height
