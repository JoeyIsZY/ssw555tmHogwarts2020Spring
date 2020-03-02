'''us09 
Fangji Liang 2/28/2020'''


def us09_birth_after_death(repos):
    '''Child should be born before death of mother and before 9 months after death of father'''
    err = []
    for fam in repos.families.values():
        if fam.repo['CHIL']['detail'] != 'NA':
            for chil in fam.repo['CHIL']['detail']:
                chil_bir = repos.individuals[chil].repo['BIRT']
                if chil_bir['detail'] != 'NA':
                    wife = repos.individuals[fam.repo['WIFE']['detail']]
                    husb = repos.individuals[fam.repo['HUSB']['detail']]
                    if not wife.alive and chil_bir['detail'] > wife.repo['DEAT']['detail']:
                        err.append(('ERROR', 'FAMILY', 'US09', (wife.repo['DEAT']['line'], chil_bir['line']), fam.fam_id, f"Mother's death date {wife.repo['DEAT']['detail']:%Y-%m-%d} occurs before children birth {chil_bir['detail']:%Y-%m-%d}."))
                    if not husb.alive and (chil_bir['detail'] - husb.repo['DEAT']['detail']).days > 270:
                        err.append(('ANOMALY', 'FAMILY', 'US09', (husb.repo['DEAT']['line'], chil_bir['line']), fam.fam_id, f"Father's death date {husb.repo['DEAT']['detail']:%Y-%m-%d} occurs more than 9 month before children birth {chil_bir['detail']:%Y-%m-%d}."))
    return err
