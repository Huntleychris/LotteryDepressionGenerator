from flask import Flask, render_template, request
import random

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def lottery_simulation():
    if request.method == 'POST':
        # Get inputs from the form
        want_to_watch = request.form.get('want_to_watch', 'n').lower()
        feeling_lucky = request.form.get('feeling_lucky', 'n').lower()
        show_me_now = request.form.get('show_me_now', 'n').lower()
        best_guess = int(request.form.get('best_guess', 1))
        how_many = int(request.form.get('how_many', 1))
        car_payments = int(request.form.get('car_payments', 1))
        job_hate = int(request.form.get('job_hate', 1))
        minutes_to_leave = int(request.form.get('minutes_to_leave', 1))
        avg_iq_ofcoworkers = int(request.form.get('avg_iq_ofcoworkers', 1))

        # Prepare inputs for Powerball number generation
        inputs = [how_many, car_payments, job_hate, minutes_to_leave, avg_iq_ofcoworkers]
        powerball_numbers = generate_powerball_numbers(inputs)
        powerball = generate_powerball()
        winning_number = generate_winning_number()

        # Collect results to show in the UI
        results = {
            'powerball_numbers': powerball_numbers,
            'powerball': powerball,
            'winning_number': winning_number,
            'best_guess': best_guess,
            'want_to_watch': want_to_watch,
            'show_me_now': show_me_now
        }
        return render_template('results.html', results=results)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
