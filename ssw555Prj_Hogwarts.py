'''
SSW555
Team: Hogwarts
AUthor: yzhou，Fangji Liang
'''

import os
from datetime import datetime
from prettytable import PrettyTable
from special_list import pretty_special
from error_list import pretty_error
'''
change_date_2020_2_11: change origin code from yz, Fangji Liang
change_date_2020_2_17: 1.use fp.close() 2.reset dateitem's value 3.default: self.alive = True 4. add us01 5.add us07, Haodong Wu
change_date_2020_2_18: all date will store by datetime type in repository(Individual, Family), Fangji Liang
changd_date_2020_2_18: add new function errors_print to collect and print all errors, Haodong Wu
changd_date_2020_4_10: add new function special_print to collect and print individuals and groups with characteristics, Haodong Wu
'''


class Individual:
    """ This is the class to store the information of each person. """
    pt_labels = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    def __init__(self, indi_id):
        # create the instance of individual
        self.indi_id = indi_id
        self.repo = {'BIRT': {'line': int(), 'detail': 'NA'}, 'DEAT': {'line': int(), 'detail': 'NA'},
                     'NAME': {'line': int(), 'detail': 'NA'}, 'SEX': {'line': int(), 'detail': 'NA'},
                     'FAMC': {'line': int(), 'detail': 'NA'}, 'FAMS': {'line': int(), 'detail': 'NA'}}
        self.id_line = int()
        self.alive = True
        self.age = 'NA'
    
    def __getitem__(self, key):
        return self.repo[key]
    
    def __setitem__(self, key, value):
        self.repo[key] = value
        
    def __delitem__(self, key):
        del self.repo[key]

    def set_id_line(self, id_line):
        self.id_line = id_line

    def is_alive(self):
        if self['DEAT']['detail'] != 'NA' and self['DEAT']['detail'] <= datetime.now():
            self.alive = False
        elif self['BIRT']['detail'] != 'NA' and self['BIRT']['detail'] > datetime.now():
            self.alive = False

    def get_age(self):
        # age has 2 situation and depends on person died or not
        dt1 = self['BIRT']['detail']
        if self.alive:
            dt2 = datetime.now()
        else:
            dt2 = self['DEAT']['detail']
        if dt1 != 'NA' and dt2 != 'NA':
            self.age = int((dt2 - dt1).days / 365)
        else:
            self.age = 0

    def pt_row(self):
        return (self.indi_id, self['NAME']['detail'], self['SEX']['detail'],
                f"{self['BIRT']['detail']:%Y-%m-%d}", self.age, self.alive,
                "NA" if self['DEAT']['detail'] == "NA" else f"{self['DEAT']['detail']:%Y-%m-%d}",
                self['FAMC']['detail'], self['FAMS']['detail'])


class Family:
    """ This is the class to store the information of each family. """
    pt_labels = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, fam_id):
        self.fam_id = fam_id
        self.repo = {'MARR': {'line': int(), 'detail': 'NA'}, 'DIV': {'line': int(), 'detail': 'NA'},
                     'HUSB': {'line': int(), 'detail': 'NA'}, 'WIFE': {'line': int(), 'detail': 'NA'},
                     'CHIL': {'line': int(), 'detail': 'NA'}}
        self.id_line = int()
        self.husband_name = 'NA'
        self.wife_name = 'NA'
    
    def __getitem__(self, key):
        return self.repo[key]
    
    def __setitem__(self, key, value):
        self.repo[key] = value
        
    def __delitem__(self, key):
        del self.repo[key]

    def set_id_line(self, id_line):
        self.id_line = id_line

    def set_husband_name(self, husband_name):
        self.husband_name = husband_name

    def set_wife_name(self, wife_name):
        self.wife_name = wife_name

    def pt_row(self):
        return (self.fam_id, "NA" if self['MARR']['detail'] == "NA" else f"{self['MARR']['detail']:%Y-%m-%d}",
                "NA" if self['DIV']['detail'] == "NA" else f"{self['DIV']['detail']:%Y-%m-%d}",
                self['HUSB']['detail'], self.husband_name, self['WIFE']['detail'],
                self.wife_name, self['CHIL']['detail'])


class Repository:
    '''
    Get Current Working Directory. If this not work for your pc, please hardcode the absolute path for you.
    Or make sure the ged file's path is same as this program's path
    Change ged file's name and path: test = Repository(my_path, my_file_name)
    '''
    def __init__(self, path=os.getcwd(), file_name='ssw555prj_Hogwarts_testfile.ged'):
        self.individuals = dict()
        self.families = dict()
        self.file_name = file_name
        self.path = path
        self.get_file_reader()
        self.update_individuals()
        self.update_families()

    def __str__(self):
        pt_indi = PrettyTable(field_names=Individual.pt_labels)
        for indi_id in sorted(self.individuals.keys()):
            pt_indi.add_row(self.individuals[indi_id].pt_row())
        
        pt_fam = PrettyTable(field_names=Family.pt_labels)
        for fam_id in sorted(self.families.keys()):
            pt_fam.add_row(self.families[fam_id].pt_row())

        return f"\nDETAIL INFORMATION OF INDIVIDUALS\n{pt_indi}\nDETAIL INFORMATION OF FAMILIES\n{pt_fam}"
    
    def get_file_reader(self):
        try:
            fp = open(os.path.join(self.path, self.file_name), 'r')
        except FileNotFoundError:
            raise FileNotFoundError(f'File cannot be opened.')
        else:
            indi_date = ['BIRT', 'DEAT']
            indi_no_date = ['NAME', 'SEX', 'FAMC', 'FAMS']
            fam_date = ['MARR', 'DIV']
            fam_no_date = ['HUSB', 'WIFE', 'CHIL']
            indi_id = ''
            fam_id = ''
            date_item = ''

        with fp:
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
                        self.individuals[indi_id][word[1]]['line'] = index
                        if word[1] == 'FAMS':
                            if self.individuals[indi_id][word[1]]['detail'] == 'NA':
                                self.individuals[indi_id][word[1]]['detail'] = set([' '.join(word[2:])])
                            else:
                                self.individuals[indi_id][word[1]]['detail'].add(' '.join(word[2:]))
                        else:
                            self.individuals[indi_id][word[1]]['detail'] = ' '.join(word[2:])
                    elif word[1] in fam_no_date:
                        if word[1] == 'CHIL':
                            self.families[fam_id][word[1]]['line'] = index
                            if self.families[fam_id][word[1]]['detail'] == 'NA':
                                self.families[fam_id][word[1]]['detail'] = set([' '.join(word[2:])])
                            else:
                                self.families[fam_id][word[1]]['detail'].add(' '.join(word[2:]))
                        else:
                            self.families[fam_id][word[1]]['line'] = index
                            self.families[fam_id][word[1]]['detail'] = ' '.join(word[2:])
                    else:
                        date_item = word[1]
                elif word[0] == '2':
                    if date_item in indi_date:
                        self.individuals[indi_id][date_item]['line'] = index
                        # individual keywords with date stores by datetime types
                        self.individuals[indi_id][date_item]['detail'] = datetime.strptime(' '.join(word[2:]), '%d %b %Y')
                        date_item = 'NA'
                    elif date_item in fam_date:
                        self.families[fam_id][date_item]['line'] = index
                        # families keywords with date stores by datetime type
                        self.families[fam_id][date_item]['detail'] = datetime.strptime(' '.join(word[2:]), '%d %b %Y')
                        date_item = 'NA'
                    else:
                        pass
                else:
                    pass
        fp.close()

    def update_individuals(self):
        for indi in self.individuals.values():
            indi.is_alive()
            indi.get_age()

    def update_families(self):
        for fam in self.families.values():
            if fam['HUSB']['detail'] != 'NA':
                fam.set_husband_name(
                    self.individuals[fam['HUSB']['detail']]['NAME']['detail'])
            if fam['WIFE']['detail'] != 'NA':
                fam.set_wife_name(
                    self.individuals[fam['WIFE']['detail']]['NAME']['detail'])
    

def main():
    test = Repository()
    print(test)
    print(pretty_error(test))
    print(pretty_special(test))


if __name__ == '__main__':
    main()