"""
Author: yzhou
"""


def us14_multiple_births(repo1):
    """No more than five siblings should be born at the same time."""
    error = []

    for fam in repo1.families.values():
        children = fam.repo['CHIL']['detail']
        if children != 'NA' and len(children) > 5:
            date = {}
            for child in list(children):
                child_birth = repo1.individuals[child].repo['BIRT']['detail']
                if child_birth not in date.keys() and not date:
                    date[child_birth] = 1
                elif child_birth in date.keys():
                    date[child_birth] += 1
                else:
                    for day in date.keys():
                        if abs(child_birth-day).days <= 1:
                            date[day] += 1

            for num in date.values():
                if num > 5:
                    error_message = f'Family{fam.fam_id} multiple birth more than 5!'
                    error.append(('ERROR', 'FAMILY', 'US14', fam.id_line, fam.fam_id, error_message))

    return error


