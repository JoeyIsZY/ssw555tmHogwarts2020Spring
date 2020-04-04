"""
us24_Unique families by spouses
No more than one family with the same spouses by name
and the same marriage date should appear in a GEDCOM file

Author: Ying Hu
"""


def us24_unique_families_by_spouses(repo1):
    error = []
    for fam1 in repo1.families.values():
        for fam2 in repo1.families.values():
            if (fam1 != fam2 and fam1.husband_name == fam2.husband_name and fam1.repo['MARR']['detail'] == \
                    fam2.repo['MARR']['detail'] and fam1.husband_name != 'NA' and fam2.husband_name != 'NA' and \
                    fam1.repo['MARR']['detail'] != 'NA' and fam2.repo['MARR']['detail'] != 'NA') or (fam1 != fam2 and
                    fam1.wife_name == fam2.wife_name and fam1.repo['MARR']['detail'] == fam2.repo['MARR']['detail'] and
                    fam1.wife_name != 'NA' and fam2.wife_name != 'NA' and fam1.repo['MARR']['detail'] != 'NA' and
                    fam2.repo['MARR']['detail'] != 'NA'):
                fam_id_pair = [fam1.fam_id, fam2.fam_id]
                fam_id_pair.sort()
                fam_id_line_pair = [fam1.id_line, fam2.id_line]
                fam_id_line_pair.sort()
                if len(error) == 0 and fam_id_pair not in error:
                    error.append(('ANOMALY', 'FAMILY', 'US24', tuple(fam_id_pair),
                                  tuple(fam_id_line_pair), 'Families with the same spouses by name and the same marriage date.'))
    print(error)
    return error

