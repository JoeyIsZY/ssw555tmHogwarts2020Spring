"""
us03_Birth before death
Birth should occur before death of an individual

Author: Ying Hu
"""
import datetime


def us03_birth_before_death(repo):
    error = []

    for indi in repo.individuals.values():
        birt = indi['BIRT']['detail']
        deat = indi['DEAT']['detail']
        # compare individuals' birth and death
        if birt != 'NA' and deat != 'NA' and birt > deat:
            error_message = f'Death {str(deat.strftime("%Y-%m-%d"))} occurs before birth {str(birt.strftime("%Y-%m-%d"))}.'
            error.append(('ERROR', 'INDIVIDUAL', 'US03', indi['DEAT']['line'], indi.indi_id, error_message))

    return error