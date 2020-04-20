"""Death should be less than 150 years after birth for dead people, and current date should be less than 150 years after birth for all living people
    Written by Haodong Wu   15/02/2020"""
import datetime


def us07_not_olderthan150(repo):
    """get the repo including all individuals then calculate their ages"""
    error = []

    for indi in repo.individuals.values():
        #date_birth = datetime.datetime.strptime(indi['BIRT']['detail'], '%d %b %Y')
        #because the epo['BIRT']['detail'] in main function has been changed to date type, so we don't need this formant convey
        date_birth = indi['BIRT']['detail']
        if indi.alive:
            date2 = datetime.datetime.now()
            error_message = 'More than 150 years old - Birth date: ' + str(date_birth.strftime("%Y-%m-%d")) + '.'
        
        else:
            date2 = indi['DEAT']['detail']
            if date2 != 'NA':
                error_message = 'More than 150 years old at death - Birth date: ' + str(date_birth.strftime("%Y-%m-%d")) + ', Death date: ' + str(date2.strftime("%Y-%m-%d")) + '.'
        
        if date2 != 'NA':
            if int((date2 - date_birth).days / 365) > 150:
                error.append(('ERROR','INDIVIDUAL', 'US07', indi['BIRT']['line'], indi.indi_id, error_message ))

    return error