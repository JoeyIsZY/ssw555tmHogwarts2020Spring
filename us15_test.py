'''us015 test 
Fangji Liang 3/22/2020'''


import unittest
from ssw555Prj_Hogwarts import Repository
from us15 import us15_more_than_15siblings


class US15_TestCase(unittest.TestCase):
    def test_us15(self):
        test = Repository()
        self.assertEqual(us15_more_than_15siblings(test),
                         [('ANOMALY', 'FAMILY', 'US15', 697, '@F_L_US15_1@', 'More than 15 siblings in a family, Number : 16')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)