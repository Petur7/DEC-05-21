from math import pow, sqrt


# Input a number
while True:
    try: a = float(input('Input a number: '))
    except: print('Invalid input number')
    else: break
    
# Input b number
while True:
    try: b = float(input('Input b number: '))
    except: print('Invalid input number')
    else: break

# Input c number
while True:
    try: c = float(input('Input c number: '))
    except: print('Invalid input number')
    else: break

# Solve quadratic equation
delta = pow(b, 2) - 4 * a * c
if delta < 0: 
    result = None
else: 
    first_result = (-1 * b + sqrt(delta))/(2 * a)
    second_result = (-1 * b - sqrt(delta))/(2 * a)
    result = (first_result, second_result)

# Check result
if result == None: print('Equation does not have any result.')
elif result[0] == result[1]:
    print('Equation has 1 result {}'.format(result[0]))
else:
    print('Equation has 2 results: {} and {}'.format(result[0], result[1]))
