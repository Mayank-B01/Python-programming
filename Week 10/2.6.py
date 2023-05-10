def binary_to_decimal(binary):      # defining a recursive function
    if binary == "":                # checking for empty character as a base value
        return 0
    else:
        remain = binary[:-1]        # taking the value entered except the last digit
        last = int(binary[-1])      # converting the last digit into integer
        decimal = binary_to_decimal(remain)     # calling the recursive function
        decimal = (decimal * 2) + last          # converting the binary into decimal
        return decimal


binary_num = input("Enter binary value:")
print("The decimal of", binary_num, "is:", binary_to_decimal(binary_num))
