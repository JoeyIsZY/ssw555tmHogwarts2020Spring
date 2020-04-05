'''us015 test 
Fangji Liang 3/22/2020'''
import os
import unittest
from ssw555Prj_Hogwarts import Repository
from us16 import us16_same_male_surname


class US16_TestCase(unittest.TestCase):
    def test_us16(self):
        path = os.getcwd()
        test = Repository()
        test.get_file_reader(path)
        test.update_individuals()
        test.update_families()
        self.assertEqual(sorted(us16_same_male_surname(test)), [('ANOMALY', 'FAMILY', 'US16', 188, '@F3@', "Male Child's surname: Snow is different with father's surname: Stark"),
                                                        ('ANOMALY', 'FAMILY', 'US16', 460, '@F_W_US18_1@', "Male Child's surname: Incest is different with father's surname: Poor"),
                                                        ('ANOMALY', 'FAMILY', 'US16', 724, '@F_Z_US13_1@', "Male Child's surname: Fu is different with father's surname: Gu"),
                                                        ('ANOMALY', 'FAMILY', 'US16', 724, '@F_Z_US13_1@', "Male Child's surname: Lan is different with father's surname: Gu")])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
