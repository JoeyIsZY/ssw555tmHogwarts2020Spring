"""
Testing for us04
Author: yzhou
"""
import unittest
from ssw555Prj_Hogwarts import Repository
from us04 import us04_marriage_before_divorce


class US04_TestCase(unittest.TestCase):
    def test_us04(self):
        test = Repository()
        self.assertEqual(us04_marriage_before_divorce(test),
                         [('ERROR', 'FAMILY', 'US04', 235, '@F_Z_US04_1@', 'Family @F_Z_US04_1@ has no marriage date. '),
                          ('ERROR', 'FAMILY', 'US04', (238, 242, 244), '@F_Z_US04_2@',
                           'Family @F_Z_US04_2@ marriage date is after than divorce date. '),
                         ('ERROR', 'FAMILY', 'US04', (278, 282, 284), '@F_Z_US05_2@',
                          'Family @F_Z_US05_2@ marriage date is after than divorce date. ')])

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
