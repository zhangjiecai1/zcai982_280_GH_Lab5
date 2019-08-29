# Zhangjie Cai zcai982
import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        #arrange
        a = maths.add(1,2)
        #assert
        self.assertEqual(a, 3)
        '''task 2'''
        #arrange
        e = maths.add(1, 2, 2)
        f = maths.add(10, 20, 15)
        #assert
        self.assertEqual(e, 11)
        self.assertEqual(f, 20)

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        #arrange
        b = maths.fibonacci(5)
        #assert
        self.assertEqual(b, 5)
        
    def test_convert_base(self):
        #arrange
        c = maths.convert_base(32, 2)
        d = maths.convert_base(32, 16)
        #assert
        self.assertEqual(int(c), 100000)
        self.assertEqual(int(d), 20)

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
