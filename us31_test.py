"""
Author: yzhou
"""
import unittest
from ssw555Prj_Hogwarts import Repository
from us31 import us31_list_living_single


class MyTestCase(unittest.TestCase):
    def test_list_living_single(self):
        test = Repository()
        self.assertEqual(us31_list_living_single(test), ('People who are single over 30', ['@I_W_US07_1@', '@I_Z_US14_1@', '@I_Z_US14_2@']))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)