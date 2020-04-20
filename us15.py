'''us015 
Fangji Liang 3/22/2020'''


def us15_more_than_15siblings(repos):
    '''There should be fewer than 15 siblings in a family'''
    err = []
    for fam in repos.families.values():
        chils = fam['CHIL']['detail']
        if chils != 'NA' and len(chils) > 15:
                err.append(('ANOMALY', 'FAMILY', 'US15', fam['CHIL']['line'], fam.fam_id, f"More than 15 siblings in a family, Number : {len(chils)}"))
    return err