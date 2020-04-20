"""This is a test file for us06.py
    Written by Ying Hu   02/24/2020
"""
import unittest
from us06 import us06_divorce_before_death
from ssw555Prj_Hogwarts import Repository


class Testdivorce_before_death(unittest.TestCase):
    def test_divorce_before_marriage(self):
        test = Repository()
        self.assertEqual(us06_divorce_before_death(test), [('ERROR', 'FAMILY', 'US06', 479, '@F_H_US06_1@',
                                                     'Divorce date 1712-01-01 occurs after husband death 1700-11-10.'),
                                                      ('ERROR', 'FAMILY', 'US06', 479, '@F_H_US06_1@',
                                                        'Divorce date 1712-01-01 occurs after wife death 1711-11-10.')])


if __name__ == '__main__':
    unittest.main()
