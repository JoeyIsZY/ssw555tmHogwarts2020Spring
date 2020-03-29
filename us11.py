"""
Author: yzhou
"""


def us11_no_bigamy(repo1):
    """ Marriage should not occur during marriage to another spouse."""

    error = []
    fam_list = list(repo1.families.values())
    i = 1
    for fam_1 in fam_list:
        for fam_2 in fam_list[i:]:
            if fam_1.fam_id != fam_2.fam_id:
                if fam_1.repo['HUSB']['detail'] == fam_2.repo['HUSB']['detail']:
                    if (fam_1.repo['DIV']['detail'] == 'NA' and fam_2.repo['DIV']['detail'] == 'NA') or (
                            fam_1.repo['MARR']['detail'] < fam_2.repo['MARR']['detail'] < fam_1.repo['DIV']['detail']):
                        error_message = f"Husband:<{fam_1.repo['HUSB']['detail']}> has one more spouse."
                        error.append(('ERROR', 'INDIVIDUAL', 'US11',
                                      (fam_1.repo['HUSB']['line'], fam_2.repo['HUSB']['line']),
                                      fam_1.repo['HUSB']['detail'],
                                      error_message))
                if fam_1.repo['WIFE']['detail'] == fam_2.repo['WIFE']['detail']:
                    if (fam_1.repo['DIV']['detail'] == 'NA' and fam_2.repo['DIV']['detail'] == 'NA') or (
                            fam_1.repo['MARR']['detail'] < fam_2.repo['MARR']['detail'] < fam_1.repo['DIV']['detail']):
                        error_message = f"Wife:<{fam_1.repo['WIFE']['detail']}> has one more spouse."
                        error.append(('ERROR', 'INDIVIDUAL', 'US11',
                                      (fam_1.repo['WIFE']['line'], fam_2.repo['WIFE']['line']),
                                      fam_1.repo['WIFE']['detail'],
                                      error_message))

    return error
