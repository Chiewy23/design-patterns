import unittest
from bridge.bridge import SalesDepartment, FullTimeEmployee, ITDepartment, PartTimeEmployee

'''
Bridge: Decouples an abstraction from its implementation so the two can vary independently.
'''


class TestMain(unittest.TestCase):
    def setUp(self):
        print("----- Bridge Setup -----")
        self.sales_department = SalesDepartment(FullTimeEmployee())
        self.it_department = ITDepartment(PartTimeEmployee())

    def test_adapter(self):
        self.sales_department.assign_employee()
        self.it_department.assign_employee()

        self.assertEqual(self.sales_department.get_employee_count(), 1)
        self.assertEqual(self.it_department.get_employee_count(), 1)

    def tearDown(self):
        print("----- Bridge Teardown -----")


if __name__ == '__main__':
    unittest.main()

# Run all tests in all files:
# python3 -m unittest

# More detail:
# python3 -m unittest -v
