class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        """
        This method finds the length of line.

        Args:
            No
        Returns:
            float or int: distance.
        """
        distance = math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        return distance
    x1, y1 = 1, 2
    x2, y2 = 4, 6
    my_line = Line(x1, y1, x2, y2)
    length = my_line.get_length()
    print(f"Length of the line: {length}")