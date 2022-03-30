import unittest
# import calculator import add
import calculator

class TestCalculatorApp(unittest.TestCase):

    def test_add_function(self):
        self.assertEqual(calculator.add(4,3), 7, '''An add function is defined 
        that takes in two numbers as arguments 
        and returns the sum''')

    def test_subtract_function(self):
        self.assertEqual(calculator.subtract(4,3), 1, '''A subtract function is defined 
        that takes in two numbers as arguments 
        and returns the difference''')

if __name__ == '__main__':
    unittest.main()