class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        '''Create serial number generator from starting number'''
        self.start = start
        self.last_num_given = start - 1

    def generate(self):
        '''increments the serial number by 1 every time it is called'''
        self.last_num_given += 1
        return self.last_num_given

    def reset(self):
        '''when called resets the counter to original start num'''
        self.last_num_given = self.start - 1

#counter more explict