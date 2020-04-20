"""
    uesr story 25: No more than one child with the same name and birth date should appear in a family
    Written by Haodong Wu   05/04/2020
"""
def us25_unique_first_names_in_families(repo):
    """No more than one child with the same name and birth date should appear in a family"""
    error = []

    for fam in repo.families.values():
        children = fam['CHIL']['detail']
        fam_id = fam.fam_id
        fam_line = fam['CHIL']['line']
        if children != 'NA' and len(children) > 1:
            children_dic = {}
            for child in list(children):
                child_birth = repo.individuals[child]['BIRT']['detail']
                child_name = repo.individuals[child]['NAME']['detail']
                if child_name not in children_dic:
                    children_dic[child_name] = {}
                if child_birth not in children_dic[child_name]:
                    children_dic[child_name][child_birth] = set()
                    children_dic[child_name][child_birth].add(child)
                else:
                    children_dic[child_name][child_birth].add(child)
            for name in children_dic.keys():
                for date in children_dic[name]:
                    if len(children_dic[name][date]) > 1:
                        error_message = f'Individuals {sorted(children_dic[name][date])} have same name {name} and same birthday {date:%Y-%m-%d}!'
                        error.append(('ANOMALY','FAMILY', 'US25', fam_line, fam.fam_id, error_message ))

    return error