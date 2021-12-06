# Get first number
while True:
    try: first_number = float(input('Input first number: '))
    except: print('Invalid input number')
    else: break

# Get second number
while True:
    try: second_number = float(input('Input second number: '))
    except: print('Invalid input number')
    else: break

# Get third number
while True:
    try: third_number = float(input('Input third number: '))
    except: print('Invalid input number')
    else: break

# Get largest number
largest_number = max(first_number, second_number, third_number)

# Print result
print(f'The biggest number between {first_number}, {second_number}, and {third_number} is {largest_number}')
