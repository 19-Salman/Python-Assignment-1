# Function to print pyramid pattern
def print_pyramid(n):
    # Outer loop for each row
    for i in range(n):
        # Print spaces before the stars in each row
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print stars for the current row
        for k in range(2 * i + 1):
            print("*", end="")
        
        # Move to the next line after each row
        print()

# Number of rows in the pyramid
n = int(input("Enter the number of rows: "))

# Call the function to print the pyramid
print_pyramid(n)
