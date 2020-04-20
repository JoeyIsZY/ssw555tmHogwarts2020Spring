"""
Author: yzhou
"""


def us11_no_bigamy(repo):
    """ Marriage should not occur during marriage to another spouse."""

    error = []
    fam_list = list(repo.families.values())
    i = 1
    for fam_1 in fam_list:
        for fam_2 in fam_list[i:]:
            if fam_1.fam_id != fam_2.fam_id:
                if fam_1['HUSB']['detail'] == fam_2['HUSB']['detail']:
                    if (fam_1['DIV']['detail'] == 'NA' and fam_2['DIV']['detail'] == 'NA') or (
                            fam_1['MARR']['detail'] < fam_2['MARR']['detail'] < fam_1['DIV']['detail']):
                        error_message = f"Husband:<{fam_1['HUSB']['detail']}> has one more spouse."
                        error.append(('ERROR', 'INDIVIDUAL', 'US11',
                                      (fam_1['HUSB']['line'], fam_2['HUSB']['line']),
                                      fam_1['HUSB']['detail'],
                                      error_message))
                if fam_1['WIFE']['detail'] == fam_2['WIFE']['detail']:
                    if (fam_1['DIV']['detail'] == 'NA' and fam_2['DIV']['detail'] == 'NA') or (
                            fam_1['MARR']['detail'] < fam_2['MARR']['detail'] < fam_1['DIV']['detail']):
                        error_message = f"Wife:<{fam_1['WIFE']['detail']}> has one more spouse."
                        error.append(('ERROR', 'INDIVIDUAL', 'US11',
                                      (fam_1['WIFE']['line'], fam_2['WIFE']['line']),
                                      fam_1['WIFE']['detail'],
                                      error_message))
        i += 1

    return error
