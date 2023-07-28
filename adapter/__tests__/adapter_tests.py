import unittest
from adapter.adapter import Adapter

'''
Adapter: Converts the interface of a class into another interface the client expects.
Adapter lets classes work together which couldn't otherwise due to incompatible interfaces.
'''


class TestMain(unittest.TestCase):
    def setUp(self):
        print("----- Adapter Setup -----")
        self.adapter = Adapter()

    def test_adapter(self):
        result = self.adapter.connect_to_file_system(543)
        self.assertEqual(result, 55)

    def tearDown(self):
        print("----- Adapter Teardown -----")


if __name__ == '__main__':
    unittest.main()

# Run all tests in all files:
# python3 -m unittest

# More detail:
# python3 -m unittest -v
