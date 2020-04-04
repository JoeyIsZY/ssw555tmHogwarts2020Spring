"""
us23_Unique name and birth date
No more than one individual with the same name
and birth date should appear in a GEDCOM file

Author: Ying Hu
"""


def us23_unique_name_birth_date(repo1):
    error = []
    """
    for indi1 in repo1.individuals.values():
        if indi1.repo['NAME']['detail'] != 'NA' and indi1.repo['BIRT']['detail'] != 'NA':
           for indi2 in repo1.individuals.values():
                if indi1 != indi2 and indi2.repo['NAME']['detail'] != 'NA' and indi2.repo['BIRT']['detail'] != 'NA':
                    if indi1.repo['NAME']['detail'] == indi2.repo['NAME']['detail'] and indi1.repo['BIRT']['detail'] == indi2.repo['BIRT']['detail']:
                        error.append(('ANOMALY', 'INDIVIDUAL', 'US23', (indi1.id_line, indi2.id_line),
                                      (indi1.indi_id, indi2.indi_id), 'Individuals have same name and birth date'))
                        return error
    """

    for indi1 in repo1.individuals.values():
        for indi2 in repo1.individuals.values():
            if indi1 != indi2 and indi1.repo['NAME']['detail'] == indi2.repo['NAME']['detail'] and \
                    indi1.repo['NAME']['detail'] != 'NA' and indi2.repo['NAME']['detail'] != 'NA' and \
                    indi1.repo['BIRT']['detail'] == indi2.repo['BIRT']['detail'] and indi1.repo['BIRT']['detail'] !='NA'\
                    and indi2.repo['BIRT']['detail'] != 'NA':
                fam_id_pair = [indi1.indi_id, indi2.indi_id]
                fam_id_pair.sort()
                fam_id_line_pair = [indi1.id_line, indi2.id_line]
                fam_id_line_pair.sort()
                if len(error) == 0 and fam_id_pair not in error:
                    error.append(('ANOMALY', 'INDIVIDUAL', 'US23', tuple(fam_id_line_pair), tuple(fam_id_pair),
                                  'Individuals have same name and birth date'))

    return error
