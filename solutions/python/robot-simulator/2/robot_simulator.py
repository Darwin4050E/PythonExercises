"""SOlution to robot_simulator exercise.
"""

EAST = 1
NORTH = 0
WEST = 3
SOUTH = 2

class Robot:
    """Create a Robot objet with a direction and coordinates.

    Methods
    -------
    move(instructions): modifies the direction and coordinates of the robot according to the given instructions.
    """

    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    
    def move(self, instructions):
        """Modify the direction and coordinates of the robot according to the given instructions.

        :param instructions: str - a combination of R (Turn right), L (Turn left), and A (Advance).
        :return: None
        """
        for instruction in instructions:
            if instruction == "R":
                self.direction = (self.direction + 1) % 4
            if instruction == "A":
                value = [0, 0]
                if self.direction == NORTH:
                    value = [0, 1]
                if self.direction == EAST:
                    value = [1, 0]
                if self.direction == SOUTH:
                    value = [0, -1]
                if self.direction == WEST:
                    value = [-1, 0]
                self.coordinates = (self.coordinates[0] + value[0], self.coordinates[1] + value[1])
            if instruction == "L":
                self.direction = (self.direction - 1) % 4