"""
Author: yzhou
"""
import unittest
from ssw555Prj_Hogwarts import Repository
from us14 import us14_multiple_births


class MyTestCase(unittest.TestCase):
    def test_multiple_births(self):
        test = Repository()
        self.assertEqual(us14_multiple_births(test), [('ERROR', 'FAMILY', 'US14', 771, '@F_Z_US14_1@', 'Family@F_Z_US14_1@ multiple birth more than 5!')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
