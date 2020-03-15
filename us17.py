"""
    uesr story 17:Parents should not marry any of their children
    Written by Haodong Wu   25/02/2020
"""
def us17_no_marriages_to_children(repo1):
    """get the repo including all individuals and familys """
    error = []
    for fam in repo1.families.values():
        if fam.repo['CHIL']['detail'] != 'NA':
            for child in fam.repo['CHIL']['detail']:
                for fam2 in repo1.families.values():
                    if fam.repo['HUSB']['detail'] == fam2.repo['HUSB']['detail'] and child == fam2.repo['WIFE']['detail']:
                        error_message = 'Father ' + fam. repo['HUSB']['detail'] + ' was married to child ' + child
                        error.append(('ANOMALY','FAMILY', 'US17', fam2.repo['MARR']['line'], fam2.fam_id, error_message ))
                    if fam.repo['WIFE']['detail'] == fam2.repo['WIFE']['detail'] and child == fam2.repo['HUSB']['detail']:
                        error_message = 'Mother ' + fam. repo['HUSB']['detail'] + ' was married to child ' + child
                        error.append(('ANOMALY','FAMILY', 'US17', fam2.repo['MARR']['line'], fam2.fam_id, error_message ))
    return error