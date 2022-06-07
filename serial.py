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
        self.counter = start - 1

    def generate(self):
        '''increments the serial number by 1 every time it is called'''
        self.counter += 1
        return self.counter

    def reset(self):
        '''when called resets the counter to original start num'''
        self.counter = self.start - 1
