"""This is a test file for us02.py
    Written by Ying Hu   02/24/2020
"""
import unittest
from us02 import us02_birth_before_marriage
from ssw555Prj_Hogwarts import Repository


class Testbirth_before_marriage(unittest.TestCase):
    def test_birth_before_marriage(self):
        test = Repository()
        self.assertEqual(us02_birth_before_marriage(test), [('ERROR', 'FAMILY', 'US02', 209, '@F_H_US02_1@',
                                                        'Marriage date 1531-07-21 occurs before husband birth 1600-01-10.'),
                                                    ('ERROR', 'FAMILY', 'US02', 209, '@F_H_US02_1@',
                                                     'Marriage date 1531-07-21 occurs before wife birth 1600-02-11.')])


if __name__ == '__main__':
    unittest.main(exit = False, verbosity= 2)
