"""
Author: yzhou
"""


def us32_list_mutiple_births(repo1):
    """List all multiple births in a GEDCOM file."""
    list = []

    for fam in repo1.families.values():
        if len(fam.repo['CHIL']['detail']) > 1:
            list.append(fam.fam_id)
    return ('Family that has multiple births', list)