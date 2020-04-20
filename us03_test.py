"""This is a test file for us03.py
    Written by Ying Hu   02/24/2020
"""
import unittest
from us03 import us03_birth_before_death
from ssw555Prj_Hogwarts import Repository


class Testbirth_before_death(unittest.TestCase):
    def test_birth_before_death(self):
        test = Repository()
        self.assertEqual(us03_birth_before_death(test), [('ERROR', 'INDIVIDUAL', 'US03', 170, '@I_H_US03_1@', 'Death 1600-11-10 occurs before birth 1630-02-11.')])


if __name__ == '__main__':
    unittest.main(exit = False, verbosity= 2)

