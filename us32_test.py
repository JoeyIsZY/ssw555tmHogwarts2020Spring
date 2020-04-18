"""
Author: yzhou
"""
import unittest
import os
from ssw555Prj_Hogwarts import Repository
from us32 import us32_list_mutiple_births


class MyTestCase(unittest.TestCase):
    def test_list_mutiple_births(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(us32_list_mutiple_births(test), ('Family that has multiple births', ['@F2@', '@F_W_US01_1@', '@F_H_US02_1@', '@F_Z_US04_1@', '@F_Z_US04_2@', '@F_Z_US05_1@', '@F_Z_US05_2@', '@F_W_US17_2@', '@F_W_US18_1@', '@F_W_US18_2@', '@F_H_US06_1@', '@F_H_US12_1@', '@F_Z_US10_1@', '@F_L_US15_1@', '@F_Z_US13_1@', '@F_Z_US14_1@', '@F_H_US24_1@', '@F_H_US24_2@', '@F_H_US24_3@', '@F_H_US24_4@', '@F_W_US21_1@', '@F_W_US25_1@', '@F_L_US19_1@', '@F_L_US19_3@', '@F_L_US19_4@', '@F_L_US19_5@']))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)