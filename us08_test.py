'''us08 test 
Fangji Liang 2/28/2020'''


import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us08 import us08_birth_before_marriage


class US08_TestCase(unittest.TestCase):
    def test_us08(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(sorted(us08_birth_before_marriage(test)),
                         [('ANOMALY', 'FAMILY', 'US08', (326, 313), '@F_L_US08_1@', 'Marriage date 1994-02-02 occurs after children birth 1992-07-16.'),
                          ('ANOMALY', 'FAMILY', 'US08', (334, 319), '@F_L_US08_2@', 'Divorce date 1997-09-18 occurs more than 9 month before children birth 1998-07-16.'),
                          ('ANOMALY', 'FAMILY', 'US08', (509, 540), '@F_H_US12_1@', 'Divorce date 1681-01-01 occurs more than 9 month before children birth 1711-10-11.'),
                          ('ANOMALY', 'FAMILY', 'US08', (509, 550), '@F_H_US12_1@', 'Divorce date 1681-01-01 occurs more than 9 month before children birth 1712-10-22.')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
