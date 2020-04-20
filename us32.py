"""
Author: yzhou
"""


def us32_list_mutiple_births(repo):
    """List all multiple births in a GEDCOM file."""
    list = []

    for fam in repo.families.values():
        if len(fam['CHIL']['detail']) > 1:
            list.append(fam.fam_id)
    return ('Family that has multiple births', list)