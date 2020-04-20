"""
Author: yzhou
"""
import unittest
from ssw555Prj_Hogwarts import Repository
from us13 import us13_sibling_spacing


class MyTestCase(unittest.TestCase):
    def test_sibling_spacing(self):
        test = Repository()
        self.assertEqual(us13_sibling_spacing(test), [('ERROR', 'FAMILY', 'US13', 724, '@F_Z_US13_1@', '@I_Z_US13_3@ and @I_Z_US13_4@ has an error birth spacing.')])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)