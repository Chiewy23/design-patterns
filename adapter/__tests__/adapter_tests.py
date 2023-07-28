import unittest
from adapter.adapter import Adapter

'''
Adapter: Converts the interface of a class into another interface the client expects.
Adapter lets classes work together which couldn't otherwise due to incompatible interfaces.
'''


class TestMain(unittest.TestCase):
    def setUp(self):
        print("----- About to test a function -----")

    def test_adapter(self):
        # self.assertEqual(result, 15)
        pass

    def tearDown(self):
        print("----- Cleaning up -----")


if __name__ == '__main__':
    unittest.main()

# Run all tests in all files:
# python3 -m unittest

# More detail:
# python3 -m unittest -v
