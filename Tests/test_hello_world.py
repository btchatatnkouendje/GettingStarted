import unittest
from Modules import hello_world

class MyTestCase(unittest.TestCase):
    def test_hello_message(self):
        self.assertEqual("hello 2020", hello_world.hello_message())


if __name__ == '__main__':
    unittest.main()
