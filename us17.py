"""
    uesr story 17:Parents should not marry any of their children
    Written by Haodong Wu   25/02/2020
"""
def us17_no_marriages_to_children(repo):
    """get the repo including all individuals and familys """
    error = []
    for fam in repo.families.values():
        if fam['CHIL']['detail'] != 'NA':
            for child in fam['CHIL']['detail']:
                for fam2 in repo.families.values():
                    if fam['HUSB']['detail'] == fam2['HUSB']['detail'] and child == fam2['WIFE']['detail']:
                        error_message = 'Father ' + fam. repo['HUSB']['detail'] + ' was married to child ' + child
                        error.append(('ANOMALY','FAMILY', 'US17', fam2['MARR']['line'], fam2.fam_id, error_message ))
                    if fam['WIFE']['detail'] == fam2['WIFE']['detail'] and child == fam2['HUSB']['detail']:
                        error_message = 'Mother ' + fam. repo['HUSB']['detail'] + ' was married to child ' + child
                        error.append(('ANOMALY','FAMILY', 'US17', fam2['MARR']['line'], fam2.fam_id, error_message ))
    return error