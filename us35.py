"""List all people in a GEDCOM file who were born in the last 30 days
    Written by Haodong Wu   11/04/2020"""
import datetime


def us35_list_recent_births(repo):
    """get the repo including all individuals and familys then check their dates"""
    lists = []

    for indi in repo.individuals.values():
        if indi['BIRT']['detail'] != 'NA':
            date_birth = indi['BIRT']['detail']
            if ((datetime.datetime.now() - date_birth).days <= 30 and (datetime.datetime.now() - date_birth).days > 0):
                lists.append(indi.indi_id)
    return ("People who were born in the last 30 days",lists)