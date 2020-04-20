"""
us23_Unique name and birth date
No more than one individual with the same name
and birth date should appear in a GEDCOM file

Author: Ying Hu
"""


def us23_unique_name_birth_date(repo):
    error = []
    # to avoid repeated error msg, change the way of ergodic method
    indi_list = list(repo.individuals.values())
    i = 1
    for indi1 in indi_list:
        for indi2 in indi_list[i:]:
            if indi1 != indi2 and indi1['NAME']['detail'] == indi2['NAME']['detail'] and \
                    indi1['NAME']['detail'] != 'NA' and indi2['NAME']['detail'] != 'NA' and \
                    indi1['BIRT']['detail'] == indi2['BIRT']['detail'] and indi1['BIRT']['detail'] != 'NA' \
                    and indi2['BIRT']['detail'] != 'NA':
                error.append(('ANOMALY', 'INDIVIDUAL', 'US23', (indi1.id_line, indi2.id_line), (indi1.indi_id, indi2.indi_id),
                              'Individuals have same name and birth date'))
        i += 1
    return error


