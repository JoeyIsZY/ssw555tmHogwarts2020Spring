'''us020 
Fangji Liang 4/06/2020'''
import re
from us19_us20_refactory import id_find_parent_famc

def us20_a_u_marry_n_n(repos):
    '''Aunts and uncles should not marry their nieces or nephews'''
    err = []
    for fam in repos.families.values():
        husb = fam.repo['HUSB']['detail']
        wife = fam.repo['WIFE']['detail']
        if  husb != 'NA' and wife != 'NA':
            husb_grand_fam = id_find_parent_famc(repos, husb)
            wife_grand_fam = id_find_parent_famc(repos, wife)
            husb_famc = repos.individuals[husb].repo['FAMC']['detail']
            wife_famc = repos.individuals[wife].repo['FAMC']['detail']
            if (husb_famc in wife_grand_fam) or (wife_famc in husb_grand_fam):
                err.append(('ANOMALY', 'FAMILY', 'US20', fam.id_line, fam.fam_id, f"Aunts and uncles should not marry their nieces or nephews"))
    return err