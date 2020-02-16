'''
SSW555
Team: Hogwarts
AUthor: yzhou，Fangji Liang

edited by Haodong Wu at 15/02/2020:
1. close the file
2. change the default value for self.alive from NA to True
3. restore the value of date.item after every use, or it affects other individual data
4. add new feature (us01) that checks Dates (birth, marriage, divorce, death) are not be after the current date
5. add new feature (us07) that insure age is smaller than 150.
'''

import datetime
from prettytable import PrettyTable
from us01 import current_date_check
from us07 import not_olderthan150

class Individual:
    """ This is the class to store the information of each person. """
    # __slots__ = {'ID', 'Name', 'Gender', 'Birthday', 'Age',
    #              'Alive', 'Death', 'Child', 'Spouse'}
    pt_labels = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    def __init__(self, indi_id):
        # create the instance of individual
        self.indi_id = indi_id
        self.repo = {'BIRT': {'line': int(), 'detail': 'NA'}, 'DEAT': {'line': int(), 'detail': 'NA'},
                     'NAME': {'line': int(), 'detail': 'NA'}, 'SEX': {'line': int(), 'detail': 'NA'},
                     'FAMC': {'line': int(), 'detail': 'NA'}, 'FAMS': {'line': int(), 'detail': 'NA'}}
        self.id_line = int()
        self.alive = True
        #because if a person is alive, there is no any line can swith the self.alive from 'NA' to False, I changed it 
        #The original value by yzhou is 'NA', changed by Haodong Wu during sprint1  at 15/02/2020
        self.age = 'NA'

    def set_id_line(self, id_line):
        #print(self.repo['NAME']['detail'])
        self.id_line = id_line

    def set_alive(self, alive):
        self.alive = alive

    def get_age(self):
        # age has 2 situation and depends on person died or not
        dt1 = datetime.datetime.strptime(
            self.repo['BIRT']['detail'], '%d %b %Y')
        if self.alive:
            dt2 = datetime.datetime.now()
        else:
            dt2 = datetime.datetime.strptime(
                self.repo['DEAT']['detail'], '%d %b %Y')
        self.age = int((dt2 - dt1).days / 365)

    def pt_row(self):
        return (self.indi_id, self.repo['NAME']['detail'], self.repo['SEX']['detail'], 
                self.repo['BIRT']['detail'], self.age, self.alive, self.repo['DEAT']['detail'], 
                self.repo['FAMC']['detail'], self.repo['FAMS']['detail'])


class Family:
    """ This is the class to store the information of each family. """
    # __slots__ = {'ID', 'Married', 'Divorced', 'Husband_ID', 'Husband_Name',
    #              'Wife_ID', 'Wife_Name', 'Children'}
    pt_labels = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, fam_id):
        self.fam_id = fam_id
        self.repo = {'MARR': {'line': int(), 'detail': 'NA'}, 'DIV': {'line': int(), 'detail': 'NA'},
                     'HUSB': {'line': int(), 'detail': 'NA'}, 'WIFE': {'line': int(), 'detail': 'NA'},
                     'CHIL': {'line': int(), 'detail': 'NA'}}
        self.id_line = int()
        self.husband_name = 'NA'
        self.wife_name = 'NA'

    def set_id_line(self, id_line):
        self.id_line = id_line

    def set_husband_name(self, husband_name):
        self.husband_name = husband_name

    def set_wife_name(self, wife_name):
        self.wife_name = wife_name

    def pt_row(self):
        return (self.fam_id, self.repo['MARR']['detail'], self.repo['DIV']['detail'], 
                self.repo['HUSB']['detail'], self.husband_name, self.repo['WIFE']['detail'], 
                self.wife_name, self.repo['CHIL']['detail'])


class Repository:
    def __init__(self):
        self.individuals = dict()
        self.families = dict()

    def get_file_reader(self):
        try:
            fp = open('proj03_testfile_hogwarts.ged', 'r')
        except FileNotFoundError:
            print(f'File cannot be opened.')
        else:
            indi_date = ['BIRT', 'DEAT']
            indi_no_date = ['NAME', 'SEX', 'FAMC', 'FAMS']
            fam_date = ['MARR', 'DIV']
            fam_no_date = ['HUSB', 'WIFE', 'CHIL']
            indi_id = ''
            fam_id = ''
            date_item = ''

            for index, line in enumerate(fp, 1):
                word = line.strip().split()
                if word[0] == '0':
                    if word[-1] == 'INDI':
                        indi_id = word[1]
                        self.individuals[indi_id] = Individual(indi_id)
                        self.individuals[indi_id].set_id_line(index)
                    elif word[-1] == 'FAM':
                        fam_id = word[1]
                        self.families[fam_id] = Family(fam_id)
                        self.families[fam_id].set_id_line(index)
                    else:
                        pass
                elif word[0] == '1':
                    if word[1] in indi_no_date:
                        self.individuals[indi_id].repo[word[1]]['line'] = index
                        if word[1] == 'FAMS':
                            if self.individuals[indi_id].repo[word[1]]['detail'] == 'NA':
                                self.individuals[indi_id].repo[word[1]]['detail'] = set([' '.join(word[2:])])
                            else:
                                self.individuals[indi_id].repo[word[1]]['detail'].add(' '.join(word[2:]))
                        else:
                            self.individuals[indi_id].repo[word[1]]['detail']= ' '.join(word[2:])
                    elif word[1] in fam_no_date:
                        if word[1] == 'CHIL':
                            self.families[fam_id].repo[word[1]]['line'] = index
                            if self.families[fam_id].repo[word[1]]['detail'] == 'NA':
                                self.families[fam_id].repo[word[1]]['detail'] = set([' '.join(word[2:])])
                            else:
                                self.families[fam_id].repo[word[1]]['detail'].add(' '.join(word[2:]))
                        else:
                            self.families[fam_id].repo[word[1]]['line'] = index
                            self.families[fam_id].repo[word[1]]['detail'] = ' '.join(word[2:])
                    else:
                        date_item = word[1]
                elif word[0] == '2':
                    if date_item in indi_date:
                        if date_item == 'DEAT':
                            self.individuals[indi_id].set_alive(False)
                        self.individuals[indi_id].repo[date_item]['line'] = index
                        self.individuals[indi_id].repo[date_item]['detail'] = ' '.join(word[2:])
                        date_item = 'NA'
                        #the original code doesn't have this line code, So after each use, the date_item is still there. 
                        # But coincidently every individual last level2 data is death 
                        # So this error will not occur until one individual still alive
                        # It took me two hours to find out the bug (ToT)
                    elif date_item in fam_date:
                        self.families[fam_id].repo[date_item]['line'] = index
                        self.families[fam_id].repo[date_item]['detail'] = ' '.join(word[2:])
                        date_item = 'NA'
                    else:
                        pass
                else:
                    pass
            fp.close()
            #should close the file

    def update_individuals(self):
        for indi in self.individuals.values():
            indi.get_age()

    def update_families(self):
        for fam in self.families.values():
            if fam.repo['HUSB']['detail'] != 'NA':
                fam.set_husband_name(
                    self.individuals[fam.repo['HUSB']['detail']].repo['NAME']['detail'])
            if fam.repo['WIFE']['detail'] != 'NA':
                fam.set_wife_name(
                    self.individuals[fam.repo['WIFE']['detail']].repo['NAME']['detail'])

    def table_individual(self):
        pt = PrettyTable(field_names=Individual.pt_labels)
        for indi_id in sorted(self.individuals.keys()):
            pt.add_row(self.individuals[indi_id].pt_row())
        print(pt)

    def table_family(self):
        pt = PrettyTable(field_names=Family.pt_labels)
        for fam_id in sorted(self.families.keys()):
            pt.add_row(self.families[fam_id].pt_row())
        print(pt)


def main():
    test = Repository()
    test.get_file_reader()
    test.update_individuals()
    test.update_families()
    test.table_individual()
    test.table_family()
    current_date_check(test)
    not_olderthan150(test)
if __name__ == '__main__':
    main()
