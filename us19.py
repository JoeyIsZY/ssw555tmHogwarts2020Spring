'''us019 
Fangji Liang 4/06/2020'''
import re
from us19_us20_refactory import id_find_parent_famc

def us19_first_cousin_not_marry(repos):
    '''First cousins should not marry'''
    err = []
    for fam in repos.families.values():
        husb = fam.repo['HUSB']['detail']
        wife = fam.repo['WIFE']['detail']
        if  husb != 'NA' and wife != 'NA':
            husb_grand_fam = id_find_parent_famc(repos, husb)
            wife_grand_fam = id_find_parent_famc(repos, wife)
            if len(husb_grand_fam.intersection(wife_grand_fam)) > 0:
                    err.append(('ANOMALY', 'FAMILY', 'US19', fam.id_line, fam.fam_id, f"First cousins should not marry"))
    return err