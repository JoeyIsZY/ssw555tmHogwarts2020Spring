"""This is a test file for us24.py
    Written by Ying Hu   03/30/2020
"""
import unittest
import os
from us23 import us23_unique_name_birth_date
from ssw555Prj_Hogwarts import Repository


class Test_us23_unique_name_birth_date(unittest.TestCase):
    def test_us23_unique_name_birth_date(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        # Get returned list sorted to match the result
        self.assertEqual(us23_unique_name_birth_date(test),
                         [('ANOMALY', 'FAMILY', 'US24', (725, 744), ('@F_H_US24_1@', '@F_H_US24_2@'),
                           'Families with the same husbands by name and the same marriage date.')])


if __name__ == '__main__':
    unittest.main()
