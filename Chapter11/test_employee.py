import unittest
from employee import Employee

class TestPayRaise(unittest.TestCase):
    
    def setUp(self):
        firstName = 'Fred'
        lastName = 'Flintstone'
        salary = 40000
        self.myEmployee= Employee(firstName, lastName, salary)
        
    def test_give_default_raise(self):
        self.myEmployee.give_raise()
        self.assertEqual(self.myEmployee.salary,45000)

    def test_give_custom_raise(self):
        self.myEmployee.give_raise(10000)
        self.assertEqual(self.myEmployee.salary,50000)


if __name__ == '__main__':
    unittest.main()