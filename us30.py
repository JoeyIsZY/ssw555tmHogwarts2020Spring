"""
us30_List living married
List all living married people in a GEDCOM file

Author: Ying Hu
"""


def us30_list_living_married(repo1):
    lists = []
    for indi in repo1.individuals.values():
        if indi.repo['DEAT']['detail'] != 'NA' and indi.repo['FAMS']['detail'] != 'NA':
            lists.append(indi.indi_id)
    return "People who are living and married", lists

