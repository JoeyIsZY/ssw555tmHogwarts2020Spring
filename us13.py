"""
Author: yzhou
"""


def us13_sibling_spacing(repo1):
    """ Birth dates of siblings should be more than 8 months apart or less than 2 days apart
    (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)"""

    error = []
    indi_list = list(repo1.individuals.values())
    i = 1

    for indi1 in indi_list:
        for indi2 in indi_list[i:]:
            if indi1.repo['FAMC']['detail'] == indi2.repo['FAMC']['detail'] and indi1.repo['FAMC']['detail'] != 'NA' and indi1 != indi2:
                indi1_birth = indi1.repo['BIRT']['detail']
                indi2_birth = indi2.repo['BIRT']['detail']
                if 2 < abs(indi1_birth - indi2_birth).days < 240:
                    error_message = f'{indi1.indi_id} and {indi2.indi_id} has an error birth spacing.'
                    error.append(('ERROR', 'FAMILY', 'US13', repo1.families[indi1.repo['FAMC']['detail']].id_line, indi1.repo['FAMC']['detail'], error_message))
        i += 1

    return error

