"""
    uesr story 21: Husband in family should be male and wife in family should be female
    Written by Haodong Wu   05/04/2020
"""
def us21_correct_gender_for_role(repo):
    """get the repo including all individuals and familys then return the family in which Husband or Wife has a wrong genfer.
    """
    error = []
    for fam in repo.families.values():
        husb = fam['HUSB']['detail']
        wife = fam['WIFE']['detail']
        gender_of_husb = repo.individuals[husb]['SEX']['detail']
        gender_of_wife = repo.individuals[wife]['SEX']['detail']
        if gender_of_husb != 'M':
            error_message = 'Husband ' + husb + ' in family ' + fam.fam_id + ' should be male'
            error.append(('ANOMALY','FAMILY', 'US21', repo.individuals[husb]['SEX']['line'], fam.fam_id, error_message ))
        if gender_of_wife != 'F':
            error_message = 'Wife ' + wife + ' in family ' + fam.fam_id + ' should be female'
            error.append(('ANOMALY','FAMILY', 'US21', repo.individuals[wife]['SEX']['line'], fam.fam_id, error_message ))
    return error