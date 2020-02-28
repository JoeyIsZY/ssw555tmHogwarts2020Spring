"""Check Dates (birth, marriage, divorce, death) are not be after the current date
    Written by Haodong Wu   15/02/2020"""
import datetime


def us01_current_date_check(repo1):
    """get the repo including all individuals and familys then check their dates"""
    error = []

    for indi in repo1.individuals.values():
        if indi.repo['BIRT']['detail'] != 'NA':
            #date_birth = datetime.datetime.strptime(indi.repo['BIRT']['detail'], '%d %b %Y')
            #because the epo['BIRT']['detail'] in main function has been changed to date type, so we don't need this formant convey
            date_birth = indi.repo['BIRT']['detail']
            if datetime.datetime.now() < date_birth:
                error_message = 'Birthday ' + str(date_birth.strftime("%Y-%m-%d")) + ' occurs in the future.'
                error.append(('ERROR','INDIVIDUAL', 'US01', indi.repo['BIRT']['line'], indi.indi_id, error_message ))
                #change the return formant to a list of ((ERROR or ANOMALY), object type, USID, line(just select the most important line),/
                # object id, error message(use your own language to describe the error. You also could learn from the TeamXXReport.xlsx))

        if indi.repo['DEAT']['detail'] != 'NA':
            date_death = indi.repo['DEAT']['detail']
            if datetime.datetime.now() < date_death:
                error_message = 'DEATH ' + str(date_death.strftime("%Y-%m-%d")) + ' occurs in the future.'
                error.append(('ERROR','INDIVIDUAL', 'US01', indi.repo['DEAT']['line'], indi.indi_id, error_message ))

    for fam in repo1.families.values():

        if fam.repo['MARR']['detail'] != 'NA':
            date_marriage = fam.repo['MARR']['detail']
            if datetime.datetime.now() < date_marriage:
                error_message = 'Marriage date ' + str(date_marriage.strftime("%Y-%m-%d")) + ' occurs in the future.'
                error.append(('ERROR','FAMILY', 'US01', fam.repo['MARR']['line'], fam.fam_id, error_message ))

        if fam.repo['DIV']['detail'] != 'NA':
            date_divorce = fam.repo['DIV']['detail']
            if datetime.datetime.now() < date_divorce:
                error_message = 'Divorce date ' + str(date_divorce.strftime("%Y-%m-%d")) + ' occurs in the future.'
                error.append(('ERROR','FAMILY', 'US01', fam.repo['DIV']['line'], fam.fam_id, error_message ))

    return error




