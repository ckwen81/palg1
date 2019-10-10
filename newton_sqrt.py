try:
    number = int(input("Find the square root of an integer: "))
    guess = float(input("Initial guess: "))
    tolerance = float(input("Tolerance: "))

    original_guess = guess
    count = 0
    previous = 0.0

    while abs(previous - guess) > tolerance:
        previous = guess
        quotient = number / guess
        guess = (quotient + guess) / 2
        count += 1

    print("Square root of {} is {}".format(number, guess))
    print("it took {} reps to get to {:8.8f} starting with a guess of {}".format(count, tolerance, original_guess))

except ValueError as e:
    print(e)
    quit(1)