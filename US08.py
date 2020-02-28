'''us08 
Fangji Liang'''


def us08_birth_before_marriage(repos):
    '''Children should be born after marriage of parents (and not more than 9 months after their divorce)'''
    err = []
    for fam in repos.families.values():
        if fam.repo['CHIL']['detail'] != 'NA' and fam.repo['MARR']['detail'] != 'NA':
            for chil in fam.repo['CHIL']['detail']:
                chil_bir = repos.individuals[chil].repo['BIRT']
                if chil_bir['detail'] != 'NA':
                    if fam.repo['MARR']['detail'] > chil_bir['detail']:
                        err.append(('ANOMALY', 'FAMILY', 'US08', (fam.repo['MARR']['line'], chil_bir['line']), fam.fam_id, f"Marriage date {fam.repo['MARR']['detail']:%Y-%m-%d} occurs after children birth {chil_bir['detail']:%Y-%m-%d}."))
                    if fam.repo['DIV']['detail'] != 'NA':
                        if (chil_bir['detail'] - fam.repo['DIV']['detail']).days > 270:
                            err.append(('ANOMALY', 'FAMILY', 'US08', (fam.repo['MARR']['line'], chil_bir['line']), fam.fam_id, f"Divorce date {fam.repo['DIV']['detail']:%Y-%m-%d} occurs more than 9 month before children birth {chil_bir['detail']:%Y-%m-%d}."))
    return err
