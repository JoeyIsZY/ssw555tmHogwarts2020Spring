"""
us29_List deceased
List all deceased individuals in a GEDCOM file

Author: Ying Hu
"""


def us29_list_deceased(repo1):
    lists = []
    for indi in repo1.individuals.values():
        if indi.repo['DEAT']['detail'] != 'NA':
            lists.append(indi.indi_id)
    return "People who were deceased", lists
