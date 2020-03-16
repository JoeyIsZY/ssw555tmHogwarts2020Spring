"""
us12_parents_not_too_old
Mother should be less than 60 years older than her children
and father should be less than 80 years older than his children

Author: Ying Hu
"""
import datetime


def us12_parents_not_too_old(repo1):
    error = []

    for fam in repo1.families.values():
        hus_id = fam.repo['HUSB']['detail']
        hus_birth = repo1.individuals[hus_id].repo['BIRT']['detail']
        wife_id = fam.repo['WIFE']['detail']
        wife_birth = repo1.individuals[wife_id].repo['BIRT']['detail']
        if fam.repo['CHIL']['detail'] != 'NA':
            for chil in fam.repo['CHIL']['detail']:
                chil_birth = repo1.individuals[chil].repo['BIRT']['detail']
                # for each child, to see if the difference between husband birthday and child birthday is more than 80
                # years
                if chil_birth != 'NA' and hus_birth != 'NA' and ((chil_birth - hus_birth).days / 365) > 80:
                    error_message = f'Age of husband is more than 80 when the child {chil} birth on {str(chil_birth.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US12', repo1.individuals[hus_id].repo['BIRT']['line'],
                                  hus_id, error_message))
                # for each child, to see if the difference between wife birthday and child birthday is more than 60
                # years
                if chil_birth != 'NA' and wife_birth != 'NA' and ((chil_birth - wife_birth).days / 365) > 60:
                    error_message = f'Age of wife is more than 60 when the child {chil} birth on {str(chil_birth.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US12', repo1.individuals[wife_id].repo['BIRT']['line'],
                                  wife_id, error_message))

    return error
