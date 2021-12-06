STUDENT_DATA = [
    '123456',
    '789101',
    '234567',
    '890123',
    '456789',
    '012345',
    '678901',
    '345678',
    '901234',
    '567890'
]


student_id = input('Input student ID: ')
if not student_id in STUDENT_DATA:
    print('Student is not in this class.')
else:
    print('Found student in class.')
    print(student_id[0:2])
