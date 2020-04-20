"""
us02_Birth before marriage
Birth should occur before marriage of an individual

Author: Ying Hu
"""
import datetime


def us02_birth_before_marriage(repo):
    error = []

    for fam in repo.families.values():
        marr = fam['MARR']['detail']
        hus_id = fam['HUSB']['detail']
        wife_id = fam['WIFE']['detail']

        for indi in repo.individuals.values():
            # compare husbands birth with marriage date
            if indi.indi_id == hus_id:
                hus_birt = indi['BIRT']['detail']
                if hus_birt != 'NA' and marr != 'NA' and marr < hus_birt:
                    error_message = f'Marriage date {str(marr.strftime("%Y-%m-%d"))} occurs before husband birth {str(hus_birt.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US02', fam['MARR']['line'], fam.fam_id, error_message))
            # compare wife birth with marriage date
            elif indi.indi_id == wife_id:
                wife_birt = indi['BIRT']['detail']
                if wife_birt != 'NA' and marr != 'NA' and marr < wife_birt:
                    error_message = f'Marriage date {str(marr.strftime("%Y-%m-%d"))} occurs before wife birth {str(wife_birt.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US02', fam['MARR']['line'], fam.fam_id, error_message))

    return error
