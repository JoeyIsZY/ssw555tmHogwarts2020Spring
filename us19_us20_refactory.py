def id_find_parent_famc(repos, id):
    grand_fam = set()
    id_famc = repos.individuals[id].repo['FAMC']['detail']
    if id_famc != 'NA':
        id_dad = repos.families[id_famc].repo['HUSB']['detail']
        id_mom = repos.families[id_famc].repo['WIFE']['detail']
        if id_dad != 'NA':
            id_grand_famc = repos.individuals[id_dad].repo['FAMC']['detail']
            if id_grand_famc != 'NA':
                grand_fam.add(repos.individuals[id_dad].repo['FAMC']['detail'])
        if id_mom != 'NA':
            id_grand_famc = repos.individuals[id_mom].repo['FAMC']['detail']
            if id_grand_famc != 'NA':
                grand_fam.add(repos.individuals[id_mom].repo['FAMC']['detail'])
    return grand_fam