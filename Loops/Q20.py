import time
# Get the starting number for the countdown
start_number = int(input("Enter the starting number for the countdown: "))
# Countdown loop
for i in range(start_number, -1, -1):
    print(i)
    time.sleep(1)  # Wait for 1 second before printing the next number
print("Countdown finished!")