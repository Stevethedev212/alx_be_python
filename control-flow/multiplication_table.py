# user for input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table from 1 to 10
for i in range(1, 18):
    print(f"{number} * {i} = {number * i}")
