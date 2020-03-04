"""
Testing for us04
Author: yzhou
"""
import os
import unittest
import sys 
sys.path.append(os.path.join(os.getcwd(), '.'))
#in order to import file from different folder, we need add add a new path
from ssw555Prj_Hogwarts import Repository
from us04 import us04_marriage_before_divorce


class US04_TestCase(unittest.TestCase):
    def test_us04(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us04_marriage_before_divorce(test),
                         [('ERROR', 'FAMILY', 'US04', 235, '@F_Z_US04_1@', 'Family @F_Z_US04_1@ has no marriage date. '),
                          ('ERROR', 'FAMILY', 'US04', (238, 242, 244), '@F_Z_US04_2@',
                           'Family @F_Z_US04_2@ marriage date is after than divorce date. ')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
