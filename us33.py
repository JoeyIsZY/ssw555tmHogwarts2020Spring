'''us33
Fangji Liang 4/19/2020'''

def us33_list_orphans(repos):
    '''orphan children'''

    for indi in repos.individuals.values():
        if indi.age < 18:
            if indi['FAMC']['detail'] == 'NA':
                yield indi.indi_id
            else:
                dad = repos.individuals[repos.families[indi['FAMC']['detail']]['HUSB']['detail']]
                mom = repos.individuals[repos.families[indi['FAMC']['detail']]['WIFE']['detail']]
                if not mom.alive and not dad.alive:
                    yield indi.indi_id