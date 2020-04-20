"""
us12_parents_not_too_old
Mother should be less than 60 years older than her children
and father should be less than 80 years older than his children

Author: Ying Hu
"""
import datetime


def us12_parents_not_too_old(repo):
    error = []

    for fam in repo.families.values():
        hus_id = fam['HUSB']['detail']
        hus_birth = repo.individuals[hus_id]['BIRT']['detail']
        wife_id = fam['WIFE']['detail']
        wife_birth = repo.individuals[wife_id]['BIRT']['detail']
        if fam['CHIL']['detail'] != 'NA':
            for chil in fam['CHIL']['detail']:
                chil_birth = repo.individuals[chil]['BIRT']['detail']
                # for each child, to see if the difference between husband birthday and child birthday is more than 80
                # years
                if chil_birth != 'NA' and hus_birth != 'NA' and ((chil_birth - hus_birth).days / 365) > 80:
                    error_message = f'Age of husband is more than 80 when the child {chil} birth on {str(chil_birth.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US12', repo.individuals[hus_id]['BIRT']['line'],
                                  hus_id, error_message))
                # for each child, to see if the difference between wife birthday and child birthday is more than 60
                # years
                if chil_birth != 'NA' and wife_birth != 'NA' and ((chil_birth - wife_birth).days / 365) > 60:
                    error_message = f'Age of wife is more than 60 when the child {chil} birth on {str(chil_birth.strftime("%Y-%m-%d"))}.'
                    error.append(('ERROR', 'FAMILY', 'US12', repo.individuals[wife_id]['BIRT']['line'],
                                  wife_id, error_message))

    return error

