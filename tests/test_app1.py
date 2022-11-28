import unittest
from my_app1.app1 import my_func1

class TestApp1(unittest.TestCase):
    def test_func1(self):
        self.assertEqual(my_func1(), "my application works!")

    def test_func1_again(self):
        # Test it 100 times!
        for x in range(100):
            self.assertEqual(my_func1(), "my application works!")


if __name__ == '__main__':
    unittest.main()
