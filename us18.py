"""
    uesr story 18: Siblings should not marry one another
    Written by Haodong Wu   25/02/2020
"""
def us18_no_marriages_between_siblings(repo1):
    """get the repo including all individuals and familys """
    error = []

    for indi in repo1.individuals.values():
        for indi2 in repo1.individuals.values():
            if indi.repo['FAMC']['detail'] == indi2.repo['FAMC']['detail'] and indi.repo['FAMC']['detail'] != 'NA' and indi != indi2 and indi.repo['FAMS']['detail'] != 'NA':
                family_id = [i for i in indi.repo['FAMS']['detail'] if i in indi2.repo['FAMS']['detail']]
                if len(family_id) != 0:
                    error_message = 'Siblings ' + indi.indi_id + ' and ' + indi2.indi_id + ' married'
                    for fam in repo1.families.values():
                        if fam.fam_id == family_id[0]:
                            if len(error) != 0:
                                for i in error:
                                    if i[3] != str(fam.repo['MARR']['line']):
                                #because I use individuals to get the incest situation, if I don't check, it will add two times from husband and wife
                                        error.append(('ANOMALY', 'FAMILY', 'US18', str(fam.repo['MARR']['line']), fam.fam_id, error_message))
                            else:
                                #error.append(('ANOMALY','FAMILY', 'US18', fam.repo['MARR']['line'], fam.fam_id, error_message))
                                error.append(('ANOMALY', 'FAMILY', 'US18', str(fam.repo['MARR']['line']), fam.fam_id, error_message))
                                #error.append('1')
    return error