"""
    uesr story 21: Husband in family should be male and wife in family should be female
    Written by Haodong Wu   05/04/2020
"""
def us21_correct_gender_for_role(repo1):
    """get the repo including all individuals and familys then return the family in which Husband or Wife has a wrong genfer.
    """
    error = []
    for fam in repo1.families.values():
        husb = fam.repo['HUSB']['detail']
        wife = fam.repo['WIFE']['detail']
        gender_of_husb = repo1.individuals[husb].repo['SEX']['detail']
        gender_of_wife = repo1.individuals[wife].repo['SEX']['detail']
        if gender_of_husb != 'M':
            error_message = 'Husband ' + husb + ' in family ' + fam.fam_id + ' should be male'
            error.append(('ANOMALY','FAMILY', 'US21', repo1.individuals[husb].repo['SEX']['line'], fam.fam_id, error_message ))
        if gender_of_wife != 'F':
            error_message = 'Wife ' + wife + ' in family ' + fam.fam_id + ' should be female'
            error.append(('ANOMALY','FAMILY', 'US21', repo1.individuals[wife].repo['SEX']['line'], fam.fam_id, error_message ))
    return error