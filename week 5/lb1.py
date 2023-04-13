even_sum=0
odd_sum=0
total_sum=0
for num in range(1,11):
    if num%2==0:
        even_sum +=num
    else:
        odd_sum += num

total_sum=even_sum+odd_sum
print(total_sum)
print(odd_sum)
print(even_sum)