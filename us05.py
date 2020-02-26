"""
Author: yzhou
"""


def us05_marriage_before_death(repo1):
    """ Compare marriage date and death date(if have) for each family's wife and husband. """
    error = []

    for fam in repo1.families.values():
        marriage_date = fam.repo['MARR']['detail']
        hus_id = fam.repo['HUSB']['detail']
        wife_id = fam.repo['WIFE']['detail']

        for indi in repo1.individuals.values():
            if indi.indi_id == hus_id:
                hus_ddate = indi.repo['DEAT']['detail']
                if hus_ddate != 'NA':
                    if marriage_date > hus_ddate:
                        error_message = f'Husband:<{indi.indi_id}> dead before he married. '
                        error.append(('ERROR', 'INDIVIDUAL', 'US05', (indi.repo['DEAT']['line'], fam.repo['MARR']['line']), indi.indi_id, error_message))

            if indi.indi_id == wife_id:
                wife_ddate = indi.repo['DEAT']['detail']
                if wife_ddate != 'NA':
                    if marriage_date > wife_ddate:
                        error_message = f'Wife:<{indi.indi_id}> dead before he married. '
                        error.append(('ERROR', 'INDIVIDUAL', 'US05', (indi.repo['DEAT']['line'], fam.repo['MARR']['line']), indi.indi_id, error_message))

    return error







