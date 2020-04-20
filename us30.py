"""
us30_List living married
List all living married people in a GEDCOM file

Author: Ying Hu
"""


def us30_list_living_married(repo):
    lists = []
    for indi in repo.individuals.values():
        if indi['DEAT']['detail'] != 'NA' and indi['FAMS']['detail'] != 'NA':
            lists.append(indi.indi_id)
    return "People who are living and married", lists

