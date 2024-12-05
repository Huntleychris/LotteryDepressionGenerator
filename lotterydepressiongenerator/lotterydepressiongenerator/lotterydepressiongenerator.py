import random

# Function to validate integer inputs within a range
def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

# Function to validate yes/no inputs
def get_yes_no_input(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['y', 'n']:
            return response
        else:
            print("Please enter 'y' for yes or 'n' for no.")

# Get inputs from the user
want_to_watch = get_yes_no_input('Do you want to watch it work for a winner? (y/n): ')
feeling_lucky = get_yes_no_input('Do you want some winning numbers? (y/n): ')
show_me_now = get_yes_no_input('Do you want to see your guess compared to the winner? (y/n): ')
best_guess = get_int_input('Enter a whole number between 1 and 292,000,000: ', 1, 292_000_000)
how_many = get_int_input('How many Powerball tickets did you buy for the billion-dollar drawing? (1-69): ', 1, 69)
car_payments = get_int_input('How many car payments do you have left? (1-69): ', 1, 69)
job_hate = get_int_input('How many times have you said "I hate my job" today? (1-69): ', 1, 69)
minutes_to_leave = get_int_input('How many minutes would it take for you to leave town if you won? (1-69): ', 1, 69)   
avg_iq_ofcoworkers = get_int_input('What do you think the average IQ of a coworker is? (1-69):', 1, 69)


# Generate Powerball numbers
def generate_powerball_numbers(inputs):
    powerball_numbers = set()
    for number in inputs:
        if number <= 69:
            powerball_numbers.add(number)
    while len(powerball_numbers) < 5:
        powerball_numbers.add(random.randint(1, 69))
    return sorted(powerball_numbers)

# Get the Powerball value (1-27)
def generate_powerball():
    return random.randint(1, 27)

# Generate the winning number
def generate_winning_number():
    return random.randint(1, 292_000_000)

# Prepare inputs for Powerball number generation
inputs = [how_many, car_payments, job_hate, minutes_to_leave, avg_iq_ofcoworkers]
powerball_numbers = generate_powerball_numbers(inputs)
powerball = generate_powerball()
winning_number = generate_winning_number()

# Display the Powerball ticket
print("\nYour Powerball numbers are:")
print(*powerball_numbers)
print(f"The Powerball is: {powerball}")

# Show the user's guess compared to the winning number
if show_me_now == 'y':
    print(f"Your guess: {best_guess}")
    print(f"The winning number: {winning_number}")

# Simulate the process of finding a winner
if want_to_watch == 'y':
    print("\nWatching the draw...")
    for i in range(1, 292_000_001):
        if i == winning_number:
            print("Random person wins! The winning number is:", i)
            break
        elif i == best_guess:
            print("You win! The winning number is:", i)
            break
else:
    print("\nGood choice not to watch; it would have been depressing to count to 292,000,000.")
