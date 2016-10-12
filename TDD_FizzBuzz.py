
import unittest
import FizzBuzz

class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        with self.assertRaises(TypeError):FizzBuzz.fizz_buzz()

    def testfizz_buzz_num(self):
        FB = FizzBuzz.fizz_buzz(347)
        self.assertEqual(347, FB, msg="The function should return the number if it is not divisible by 3 or 5")

    def testfizz(self):
        FB = FizzBuzz.fizz_buzz(33)
        self.assertEqual("Fizz", FB, msg="The function should return Fizz if the argument is divisible by 3")

    def testfizz_buzz(self):
        FB = FizzBuzz.fizz_buzz(300)
        self.assertEqual("FizzBuzz", FB, msg="The function should return 'FizzBuzz' if the input is divisible by 3 and 5")

    def testfizz(self):
        FB = FizzBuzz.fizz_buzz(20)
        self.assertEqual("Buzz", FB, msg="The function should return Buzz if the argument is divisible by 5")

    def testfizz_buzz_negative(self):
        FB = FizzBuzz.fizz_buzz(-300)
        self.assertEqual("FizzBuzz", FB, msg="The function should accept negative numbers")

    def testfloats(self):
        FB = FizzBuzz.fizz_buzz(20.1)
        self.assertEqual(20.1, FB, msg="The function should accept float data type")

    def testbool(self):
        FB = FizzBuzz.fizz_buzz(True)
        self.assertEqual(True, FB, msg="The function should reject booleans")

    def testlist(self):
        FB = FizzBuzz.fizz_buzz([6, 7, 8])
        self.assertEqual([6, 7, 8], FB, msg="The function should reject lists")

    def teststring(self):
        FB = FizzBuzz.fizz_buzz('string')
        self.assertEqual('string', FB, msg="The function should reject strings")

    def testdictionary(self):
        FB = FizzBuzz.fizz_buzz({"key1":"value1", "key2":"value2"})
        self.assertEqual({"key1":"value1", "key2":"value2"}, FB, msg="The function should reject dictionaries")

    def testtuple(self):
        FB = FizzBuzz.fizz_buzz((9, 8, 7))
        self.assertEqual((9, 8, 7), FB, msg="The function should reject strings")


if __name__ == '__main__':
    unittest.main()
