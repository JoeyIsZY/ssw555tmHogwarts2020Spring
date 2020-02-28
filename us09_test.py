'''us09 test 
Fangji Liang 2/28/2020'''


import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us09 import us09_birth_after_death


class US08_TestCase(unittest.TestCase):
    def test_us08(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us09_birth_after_death(test),
                         [('ERROR', 'FAMILY', 'US09', (349, 369), '@F_L_US09_1@', "Mother's death date 1995-05-04 occurs before children birth 1996-07-16."),
                          ('ANOMALY', 'FAMILY', 'US09', (357, 375), '@F_L_US09_2@', "Father's death date 1994-04-04 occurs more than 9 month before children birth 1995-07-16.")])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
