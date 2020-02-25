"""This is a test file for us03.py
    Written by Ying Hu   02/24/2020
"""
import unittest
import os
from us03 import birth_before_death
from ssw555Prj_Hogwarts import Repository


class MyTestCase(unittest.TestCase):
    def test_birth_before_death(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(birth_before_death(test), [('ERROR', 'INDIVIDUAL', 'US03', 170, '@I_H_US03_1@', 'Death 0600-11-10 occurs before birth 0630-02-11.')])


if __name__ == '__main__':
    unittest.main()

