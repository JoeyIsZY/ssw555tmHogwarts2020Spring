'''us09 
Fangji Liang 2/28/2020'''


def us09_birth_after_death(repos):
    '''Child should be born before death of mother and before 9 months after death of father'''
    err = []
    for fam in repos.families.values():
        if fam['CHIL']['detail'] != 'NA':
            for chil in fam['CHIL']['detail']:
                chil_bir = repos.individuals[chil]['BIRT']
                if chil_bir['detail'] != 'NA':
                    wife = repos.individuals[fam['WIFE']['detail']]
                    husb = repos.individuals[fam['HUSB']['detail']]
                    if not wife.alive and chil_bir['detail'] > wife['DEAT']['detail']:
                        err.append(('ERROR', 'FAMILY', 'US09', (wife['DEAT']['line'], chil_bir['line']), fam.fam_id, f"Mother's death date {wife['DEAT']['detail']:%Y-%m-%d} occurs before child {chil} birth {chil_bir['detail']:%Y-%m-%d}."))
                    if not husb.alive and (chil_bir['detail'] - husb['DEAT']['detail']).days > 270:
                        err.append(('ANOMALY', 'FAMILY', 'US09', (husb['DEAT']['line'], chil_bir['line']), fam.fam_id, f"Father's death date {husb['DEAT']['detail']:%Y-%m-%d} occurs more than 9 month before child {chil} birth {chil_bir['detail']:%Y-%m-%d}."))
    return err
