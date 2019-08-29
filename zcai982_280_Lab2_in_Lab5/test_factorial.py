import unittest     # Import the Python unit testing framework
import maths        # Our code to test

class MathsTest2(unittest.TestCase):

    def test_factorial(self):
        ''' Tests the add function. '''
        #arrange
        a = maths.factorial(4)
        #assert
        self.assertEqual(a, 24)


if __name__ == '__main__':
    unittest.main()
