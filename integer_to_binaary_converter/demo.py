def integer_to_binary(n):
    if n == 0:
        return "0"
    
    binary_representation = ""
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation
        n = n // 2
    
    return binary_representation

# Example usage
if __name__ == "__main__":
    number = int(input("Enter the number u want to convert to binary : "))
    print(f"The binary representation of {number} is {integer_to_binary(number)}")