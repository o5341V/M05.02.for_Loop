# Headers
head1 = "Number:"
head2 = "Multiplied by 2:"
head3 = "Multiplied by 10:"

# Constants used to control loop and multiplication factors.
NUM_LOOPS = 10
MULTIPLIER_2 = 2
MULTIPLIER_10 = 10

print("0 through 10 multiplied by 2 and by 10\n")
print(f"{head1:<10} {head2:<20} {head3}")

# Use a for loop to iterate through numbers 0 to NUM_LOOPS (inclusive)
for num in range(NUM_LOOPS + 1):
    multiplied_by_2 = num * MULTIPLIER_2
    multiplied_by_10 = num * MULTIPLIER_10
    print(f"{num:<10} {multiplied_by_2:<20} {multiplied_by_10}")
