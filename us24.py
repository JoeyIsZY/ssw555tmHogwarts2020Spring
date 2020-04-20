"""
us24_Unique families by spouses
No more than one family with the same spouses by name
and the same marriage date should appear in a GEDCOM file

Author: Ying Hu
"""


def us24_unique_families_by_spouses(repo):
    error = []
    # to avoid repeated error msg, change the way of ergodic method
    fam_list = list(repo.families.values())
    i = 1
    for fam1 in fam_list:
        for fam2 in fam_list[i:]:
            # if husbands in different families have the same name and same marriage date
            if fam1 != fam2 and fam1.husband_name == fam2.husband_name and fam1['MARR']['detail'] == fam2['MARR']['detail']:
                if fam1.husband_name != 'NA' and fam2.husband_name != 'NA' and fam1['MARR']['detail'] != 'NA' and fam2['MARR']['detail'] != 'NA':
                    error.append(('ANOMALY', 'FAMILY', 'US24', (fam1['MARR']['line'], fam2['MARR']['line']),
                                (fam1.fam_id, fam2.fam_id), 'Families with the same husband by name and the same marriage date.'))
            # if wives in different families have the same name and same marriage date
            elif fam1 != fam2 and fam1.wife_name == fam2.wife_name and fam1['MARR']['detail'] == fam2['MARR']['detail']:
                if fam1.wife_name != 'NA' and fam2.wife_name != 'NA' and fam1['MARR']['detail'] != 'NA' and fam2['MARR']['detail'] != 'NA':
                    error.append(('ANOMALY', 'FAMILY', 'US24', (fam1['MARR']['line'], fam2['MARR']['line']),
                                (fam1.fam_id, fam2.fam_id), 'Families with the same wife by name and the same marriage date.'))
        i += 1
    return error

