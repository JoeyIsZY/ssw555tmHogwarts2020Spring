"""
Testing for us05
Author: yzhou
"""
import os
import unittest
import sys 
sys.path.append(os.path.join(os.getcwd(), '.'))
#in order to import file from different folder, we need add add a new path
from ssw555Prj_Hogwarts import Repository
from us05 import us05_marriage_before_death


class US05_TestCase(unittest.TestCase):
    def test_us05(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us05_marriage_before_death(test), [('ERROR', 'INDIVIDUAL', 'US05', (251, 277), '@I_Z_US05_1@', 'Husband:<@I_Z_US05_1@> dead before he married. '),
                                                            ('ERROR', 'INDIVIDUAL', 'US05', (271, 282), '@I_Z_US05_4@', 'Wife:<@I_Z_US05_4@> dead before he married. ')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
