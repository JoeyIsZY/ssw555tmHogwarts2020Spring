"""Check Dates (birth, marriage, divorce, death) are not be after the current date
    Written by Haodong Wu   15/02/2020"""
import datetime

def current_date_check(repo1):
    """get the repo including all individuals and familys then convert the dates(birth, marriage, divorce, death) to datetime format"""
    error = []
    for indi in repo1.individuals.values():
        if indi.repo['BIRT']['detail'] != 'NA':
            date_birth = datetime.datetime.strptime(indi.repo['BIRT']['detail'], '%d %b %Y')
            if datetime.datetime.now() < date_birth:
                 error.append(f"ERROR! The birth date at line {indi.repo['BIRT']['line']} is {indi.repo['BIRT']['detail']} after now.")

        if indi.repo['DEAT']['detail'] != 'NA':
            date_death = datetime.datetime.strptime(indi.repo['DEAT']['detail'], '%d %b %Y')
            if datetime.datetime.now() < date_death:
                error.append(f"ERROR! The death date at line {indi.repo['DEAT']['line']} is {indi.repo['DEAT']['detail']} after now.")

    for fam in repo1.families.values():

        if fam.repo['MARR']['detail'] != 'NA':
            date_marriage = datetime.datetime.strptime(fam.repo['MARR']['detail'], '%d %b %Y')
            if datetime.datetime.now() < date_marriage:
                error.append(f"ERROR! The marriage date at line {fam.repo['MARR']['line']} is {fam.repo['MARR']['detail']} after now.")

        if fam.repo['DIV']['detail'] != 'NA':
            date_divorce = datetime.datetime.strptime(fam.repo['DIV']['detail'], '%d %b %Y')
            if datetime.datetime.now() < date_divorce:
                error.append(f"ERROR! The divorce date at line {fam.repo['DIV']['line']} is {fam.repo['DIV']['detail']} after now.")
    for item in error:
        print(item)
    return error




