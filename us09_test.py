'''us09 test 
Fangji Liang 2/28/2020'''


import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us09 import us09_birth_after_death


class US09_TestCase(unittest.TestCase):
    def test_us08(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(sorted(us09_birth_after_death(test)),
                         [('ANOMALY', 'FAMILY', 'US09', (357, 375), '@F_L_US09_2@', "Father's death date 1994-04-04 occurs more than 9 month before child @I_L_US09_6@ birth 1995-07-16."),
                          ('ANOMALY', 'FAMILY', 'US09', (522, 540), '@F_H_US12_1@', "Father's death date 1700-11-10 occurs more than 9 month before child @I_H_US12_3@ birth 1711-10-11."),
                          ('ANOMALY', 'FAMILY', 'US09', (522, 550), '@F_H_US12_1@', "Father's death date 1700-11-10 occurs more than 9 month before child @I_H_US12_4@ birth 1712-10-22."),
                          ('ERROR', 'FAMILY', 'US09', (349, 369), '@F_L_US09_1@', "Mother's death date 1995-05-04 occurs before child @I_L_US09_5@ birth 1996-07-16."),
                          ('ERROR', 'FAMILY', 'US09', (532, 550), '@F_H_US12_1@', "Mother's death date 1711-11-10 occurs before child @I_H_US12_4@ birth 1712-10-22.")])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
