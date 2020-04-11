"""List all people in a GEDCOM file who were died in the last 30 days
    Written by Haodong Wu   11/04/2020"""
import datetime


def us36_list_recent_deaths(repo1):
    """get the repo including all individuals and familys then check their dates"""
    lists = []

    for indi in repo1.individuals.values():
        if indi.repo['DEAT']['detail'] != 'NA':
            date_death = indi.repo['DEAT']['detail']
            if ((datetime.datetime.now() - date_death).days <= 30 and (datetime.datetime.now() - date_death).days > 0):
                lists.append(indi.indi_id)
    return ("People who were died in the last 30 days",lists)