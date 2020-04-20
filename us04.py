"""
Author: yzhou
"""


def us04_marriage_before_divorce(repo):
    """ Compare marriage date and divorce date(if have) for each family. """
    error = []

    for fam in repo.families.values():
        marriage_date = fam['MARR']['detail']
        divorce_date = fam['DIV']['detail']

        if marriage_date == 'NA':
            error_message = f'Family {fam.fam_id} has no marriage date. '
            error.append(('ERROR', 'FAMILY', 'US04', fam.id_line, fam.fam_id, error_message))

        if divorce_date != 'NA':
            if marriage_date > divorce_date:
                error_message = f'Family {fam.fam_id} marriage date is after than divorce date. '
                error.append(('ERROR', 'FAMILY', 'US04', (fam.id_line, fam['MARR']['line'], fam['DIV']['line']), fam.fam_id, error_message))

    return error

