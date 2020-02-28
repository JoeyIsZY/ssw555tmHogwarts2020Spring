"""
us03_Birth before death
Birth should occur before death of an individual

Author: Ying Hu
"""
import datetime


def birth_before_death(repo1):
    error = []

    for indi in repo1.individuals.values():
        birt = indi.repo['BIRT']['detail']
        deat = indi.repo['DEAT']['detail']
        # compare individuals' birth and death
        if birt != 'NA' and deat != 'NA' and birt > deat:
            error_message = f'Death {str(deat.strftime("%Y-%m-%d"))} occurs before birth {str(birt.strftime("%Y-%m-%d"))}.'
            error.append(('ERROR', 'INDIVIDUAL', 'US03', indi.repo['DEAT']['line'], indi.indi_id, error_message))

    return error