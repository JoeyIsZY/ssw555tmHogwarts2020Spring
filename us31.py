"""
Author: yzhou
"""


def us31_list_living_single(repo):
    """List all living people over 30 who have never been married in a GEDCOM file."""
    list = []

    for indi in repo.individuals.values():
        if indi.alive == True and indi['FAMS']['detail'] == 'NA' and indi.age > 30:
            list.append(indi.indi_id)
    return ('People who are single over 30', list)