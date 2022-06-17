class Rectangle:
    length: int
    width: int

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def do_area(self):
        area = self.length * self.width
        print(f"The area of the rectangle is: {area}")

    def solve_for(self, name: str):
        do = f"do_{name}"
        if hasattr(self, do) and callable(func := getattr(self, do)):
            func()
