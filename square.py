def calculate_square_area(side_length):
    """
    Calculate the area of a square given the length of its side.
    """
    return side_length ** 2

if __name__ == "__main__":
    side_length = float(input("Enter the length of the side of the square: "))
    area = calculate_square_area(side_length)
    print("The area of the square is:", area)
