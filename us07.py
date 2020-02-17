"""Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people
    Written by Haodong Wu   15/02/2020"""
import datetime

def not_olderthan150(repo1):
    """get the repo including all individuals then calculate their ages"""
    error = []
    for indi in repo1.individuals.values():
        date_birth = datetime.datetime.strptime(indi.repo['BIRT']['detail'], '%d %b %Y')
        if indi.alive:
            date2 = datetime.datetime.now()
        else:
            date2 = datetime.datetime.strptime(
                indi.repo['DEAT']['detail'], '%d %b %Y')
        if int((date2 - date_birth).days / 365) > 150:
            error.append(f"ERROR! at line {indi.repo['BIRT']['line']}, the individual who was born at {indi.repo['BIRT']['detail']} is {int((date2 - date_birth).days / 365)} years old.")
    
    for item in error:
        print(item)
    return error