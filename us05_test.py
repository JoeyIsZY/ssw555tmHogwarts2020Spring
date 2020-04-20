"""
Testing for us05
Author: yzhou
"""
import unittest
from ssw555Prj_Hogwarts import Repository
from us05 import us05_marriage_before_death


class US05_TestCase(unittest.TestCase):
    def test_us05(self):
        test = Repository()
        self.assertEqual(us05_marriage_before_death(test), [('ERROR', 'INDIVIDUAL', 'US05', (251, 277), '@I_Z_US05_1@', 'Husband:<@I_Z_US05_1@> dead before he married. '),
                                                            ('ERROR', 'INDIVIDUAL', 'US05', (271, 282), '@I_Z_US05_4@', 'Wife:<@I_Z_US05_4@> dead before he married. ')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
