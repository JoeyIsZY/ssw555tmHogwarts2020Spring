"""
us06_Divorce before death
Divorce can only occur before death of both spouses

Author: Ying Hu
"""
import datetime


def us06_divorce_before_death(repo1):
    error = []

    for fam in repo1.families.values():
        divdate = fam.repo['DIV']['detail']
        hus_id = fam.repo['HUSB']['detail']
        wife_id = fam.repo['WIFE']['detail']

        for indi in repo1.individuals.values():
            # for husbands in families, to see if the divorce date is after husbands death
            if indi.indi_id == hus_id:
                hus_deat = indi.repo['DEAT']['detail']
                if divdate != 'NA' and hus_deat != 'NA' and divdate > hus_deat:
                    error_message = f'Divorce date {str(divdate.strftime("%Y-%m-%d"))} occurs after husband death {str(hus_deat.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US06', fam.repo['DIV']['line'], fam.fam_id, error_message))
            # for wives in families, to see if the divorce date is after wives death
            elif indi.indi_id == wife_id:
                wife_deat = indi.repo['DEAT']['detail']
                if divdate != 'NA' and wife_deat != 'NA' and divdate > wife_deat:
                    error_message = f'Divorce date {str(divdate.strftime("%Y-%m-%d"))} occurs after wife death {str(wife_deat.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US06', fam.repo['DIV']['line'], fam.fam_id, error_message))

    return error
