"""This is a test file for us02.py
    Written by Ying Hu   02/24/2020
"""
import unittest
import os
from us02 import birth_before_marriage
from ssw555Prj_Hogwarts import Repository


class MyTestCase(unittest.TestCase):
    def test_birth_before_marriage(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(birth_before_marriage(test), [('ERROR', 'FAMILY', 'US02', 209, '@F_H_US02_1@',
                                                        'Marriage date 0531-07-21 occurs before husband birth 0600-01-10.'),
                                                    ('ERROR', 'FAMILY', 'US02', 209, '@F_H_US02_1@',
                                                     'Marriage date 0531-07-21 occurs before wife birth 0600-02-11.')])


if __name__ == '__main__':
    unittest.main()
