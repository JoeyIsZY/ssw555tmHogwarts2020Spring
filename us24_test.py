"""This is a test file for us24.py
    Written by Ying Hu   03/30/2020
"""
import unittest
import os
from us24 import us24_unique_families_by_spouses
from ssw555Prj_Hogwarts import Repository


class Test_us24_unique_families_by_spouses(unittest.TestCase):
    def test_us24_unique_families_by_spouses(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        # Get returned list sorted to match the result
        self.assertEqual(us24_unique_families_by_spouses(test),
                         [('ANOMALY', 'FAMILY', 'US24', (811, 830), ('@F_H_US24_1@', '@F_H_US24_2@'),
                           'Families with the same husband by name and the same marriage date.'),
                          ('ANOMALY', 'FAMILY', 'US24', (849, 868), ('@F_H_US24_3@', '@F_H_US24_4@'),
                           'Families with the same wife by name and the same marriage date.'),
                          ])


if __name__ == '__main__':
    unittest.main()
