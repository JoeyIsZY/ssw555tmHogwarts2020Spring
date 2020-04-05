"""
us24_Unique families by spouses
No more than one family with the same spouses by name
and the same marriage date should appear in a GEDCOM file

Author: Ying Hu
"""


def us24_unique_families_by_spouses(repo1):
    error = []
    fam_list = list(repo1.families.values())
    i = 1
    for fam1 in fam_list:
        for fam2 in fam_list[i:]:
            if fam1 != fam2 and fam1.husband_name == fam2.husband_name and fam1.repo['MARR']['detail'] == fam2.repo['MARR']['detail']:
                if fam1.husband_name != 'NA' and fam2.husband_name != 'NA' and fam1.repo['MARR']['detail'] != 'NA' and fam2.repo['MARR']['detail'] != 'NA':
                    error.append(('ANOMALY', 'FAMILY', 'US24', (fam1.repo['MARR']['line'], fam2.repo['MARR']['line']),
                                (fam1.fam_id, fam2.fam_id), 'Families with the same husband by name and the same marriage date.'))
            elif fam1 != fam2 and fam1.wife_name == fam2.wife_name and fam1.repo['MARR']['detail'] == fam2.repo['MARR']['detail']:
                if fam1.wife_name != 'NA' and fam2.wife_name != 'NA' and fam1.repo['MARR']['detail'] != 'NA' and fam2.repo['MARR']['detail'] != 'NA':
                    error.append(('ANOMALY', 'FAMILY', 'US24', (fam1.repo['MARR']['line'], fam2.repo['MARR']['line']),
                                (fam1.fam_id, fam2.fam_id), 'Families with the same wife by name and the same marriage date.'))
        i += 1
    return error

