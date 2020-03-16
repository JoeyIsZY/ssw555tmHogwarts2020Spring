"""This is a test file for us12.py
    Written by Ying Hu   02/25/2020
"""
import unittest
import os
from us12 import us12_parents_not_too_old
from ssw555Prj_Hogwarts import Repository


class Testparents_not_too_old(unittest.TestCase):
    def test_parents_not_too_old(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        # Get returned list sorted to match the result
        self.assertEqual(sorted(us12_parents_not_too_old(test)),
                         [('ERROR', 'FAMILY', 'US12', 520, '@I_H_US12_1@', 'Age of husband is more than 80 when the child @I_H_US12_3@ birth on 0750-10-11.'),
                          ('ERROR', 'FAMILY', 'US12', 520, '@I_H_US12_1@', 'Age of husband is more than 80 when the child @I_H_US12_4@ birth on 0790-10-22.'),
                          ('ERROR', 'FAMILY', 'US12', 530, '@I_H_US12_2@', 'Age of wife is more than 60 when the child @I_H_US12_3@ birth on 0750-10-11.'),
                          ('ERROR', 'FAMILY', 'US12', 530, '@I_H_US12_2@', 'Age of wife is more than 60 when the child @I_H_US12_4@ birth on 0790-10-22.')])


if __name__ == '__main__':
    unittest.main()
