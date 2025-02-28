import math

def calculate_cube_diagonal(edge_length):
    # Formula for the body diagonal of a cube
    diagonal = math.sqrt(3) * edge_length
    # Round the result to 2 decimal places
    return round(diagonal, 2)

def main():
    print("I will find the cube's inner diagonal for any edge length!")
    edge_length = float(input("Please enter the edge length of your cube: "))
    diagonal = calculate_cube_diagonal(edge_length)
    print(f"The length of the inner diagonal of a cube with side length {edge_length} is: {diagonal}")

if __name__ == "__main__":
    main()
