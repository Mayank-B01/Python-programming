#inputing price of bouquet of lilies and rose per piece

b_lily=int(input("Enter price of bouquet of lilies:"))
rose=int(input("Enter price of rose per piece:"))

#Calculating price of 4 roses

p_rose=4*rose
print("The total price of rose is",p_rose)

#display the money user spent

print("The total money that the user spent is:", p_rose+b_lily)
