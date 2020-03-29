"""
Testing for us10
Author: yzhou
"""
import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us10 import us10_marriage_after_14


class MyTestCase(unittest.TestCase):
    def test_us10(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us10_marriage_after_14(test), [('ANOMALY', 'FAMILY', 'US10', 235, '@F_Z_US04_1@', 'Family <@F_Z_US04_1@> do not have marriage date.'),
                                                        ('ERROR', 'INDIVIDUAL', 'US10', (249, 277), '@I_Z_US05_1@', 'Husband:<@I_Z_US05_1@> marriage before he is 14 years old.'),
                                                        ('ERROR', 'INDIVIDUAL', 'US10', (564, 570), '@I_Z_US10_2@', 'Wife:<@I_Z_US10_2@> marriage before she is 14 years old.')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
