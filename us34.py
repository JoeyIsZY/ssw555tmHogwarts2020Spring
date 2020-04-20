'''us33
Fangji Liang 4/06/2020'''


def age_large_twice(age1, age2):
    differ = abs(age1 - age2)
    min_age = min(age1, age2)
    return True if differ > min_age else False


def us34_large_age_couple(repos):
    '''Spouses whose age difference is more than twice'''
    for fam in repos.families.values():
        if fam['HUSB']['detail'] != 'NA' and fam['WIFE']['detail'] != 'NA':
            husb = repos.individuals[fam['HUSB']['detail']]
            wife = repos.individuals[fam['WIFE']['detail']]
            if husb.alive and wife.alive:
                if age_large_twice(husb.age, wife.age):
                    yield {'HUSB':husb.indi_id, 'WIFE':wife.indi_id}
            else:
                if fam['MARR']['detail'] != 'NA':
                    if husb['BIRT']['detail'] != 'NA' and wife['BIRT']['detail']:
                        husb_age = int((fam['MARR']['detail'] - husb['BIRT']['detail']).days / 365)
                        wife_age = int((fam['MARR']['detail'] - wife['BIRT']['detail']).days / 365)
                        if age_large_twice(husb_age, wife_age):
                            yield {'HUSB':husb.indi_id, 'WIFE':wife.indi_id}