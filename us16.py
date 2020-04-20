'''us016 
Fangji Liang 3/22/2020'''
import re


def us16_same_male_surname(repos):
    '''All male members of a family should have the same last name'''
    err = []
    regex = re.compile(r"(?<=\/).+?(?=\/)")
    for fam in repos.families.values():
        if  fam.husband_name != 'NA' and fam['CHIL']['detail'] != 'NA':
            husb_sur = re.findall(regex, fam.husband_name)
            for chil in fam['CHIL']['detail']:
                if repos.individuals[chil]['NAME']['detail'] != 'NA' and repos.individuals[chil]['SEX']['detail'] == 'M':
                    chil_sur = re.findall(regex, repos.individuals[chil]['NAME']['detail'])
                    if husb_sur[0] != chil_sur[0]:
                        err.append(('ANOMALY', 'FAMILY', 'US16', fam.id_line, fam.fam_id, f"Male Child's surname: {chil_sur[0]} is different with father's surname: {husb_sur[0]}"))
    return err