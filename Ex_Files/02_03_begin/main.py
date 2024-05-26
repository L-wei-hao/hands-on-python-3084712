NAMES = ['John','Paul','George', 'Ringo']
AGES = [20,21,22,23]

JOHN=NAMES[0]
PAUL=NAMES[1]

JOHN_PAUL = NAMES[:2]  #everything before index 2
GEORGE_RINGO = NAMES[2:] #everything After index 2
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]
print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE)
print(EVERY_OTHER)