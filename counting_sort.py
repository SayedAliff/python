class Area:
    def __init__(self):
        self.length = 0
        self.breadth = 0

    # Method to set dimensions
    def set_dim(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Method to calculate and return area
    def get_area(self):
        return self.length * self.breadth


if __name__ == "__main__":
    rectangle = Area()

    length = int(input("Enter length: "))
    breadth = int(input("Enter breadth: "))

    rectangle.set_dim(length, breadth)
    area = rectangle.get_area()

    print(f"Area of the rectangle: {area}")