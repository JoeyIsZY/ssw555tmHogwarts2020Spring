"""
SSW555
Team: Hogwarts
AUthor: yzhou
"""
# this is from yhu for test

import datetime
from prettytable import PrettyTable


class Individual:
    """This is the class to store the information of each person. """
    __slots__ = {'ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'}
    pt_labels = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    def __init__(self, indi_id):
        # create the instance of individual
        self.ID = indi_id
        self.Name = ''
        self.Gender = ''
        self.Birthday = ''
        self.Age = ''
        self.Alive = True
        self.Death = 'NA'
        self.Child = 'NA'
        self.Spouse = 'NA'

    def add_name(self, name):
        self.Name = name

    def add_gender(self, sex):
        self.Gender = sex

    def add_birthday(self, birth):
        self.Birthday = birth

    def add_death(self, death):
        self.Death = death

    def get_alive(self):
        self.Alive = False

    def add_child(self, fam_id):
        self.Child = fam_id

    def add_spouse(self, fam_id):
        self.Spouse = fam_id

    def get_age(self):
        # age has 2 situation and depends on person died or not
        dt1 = datetime.datetime.strptime(self.Birthday, '%d %b %Y')
        if self.Alive:
            dt2 = datetime.datetime.now()
        else:
            dt2 = datetime.datetime.strptime(self.Death, '%d %b %Y')

        self.Age = int((dt2 - dt1).days / 365)

    def pt_row(self):
        return self.ID, self.Name, self.Gender, self.Birthday, self.Age, self.Alive, self.Death, self.Child, self.Spouse


class Family:
    """This is the class to store the information of each family. """
    __slots__ = {'ID', 'Married', 'Divorced', 'Husband_ID', 'Husband_Name', 'Wife_ID', 'Wife_Name', 'Children'}
    pt_labels = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

    def __init__(self, fam_id):
        self.ID = fam_id
        self.Married = ''
        self.Divorced = ''
        self.Husband_ID = ''
        self.Husband_Name = ''
        self.Wife_ID = ''
        self.Wife_Name = ''
        self.Children = ''

    def add_married(self, married):
        self.Married = married

    def add_divorced(self, divorced):
        self.Divorced = divorced

    def add_husband_id(self, husband_id):
        self.Husband_ID = husband_id

    def add_husband_name(self, husband_name):
        self.Husband_Name = husband_name

    def add_wife_id(self, wife_id):
        self.Wife_ID = wife_id

    def add_wife_name(self, wife_name):
        self.Wife_Name = wife_name

    def add_children(self, child):
        self.Children = child

    def pt_row(self):
        return self.ID, self.Married, self.Divorced, self.Husband_ID, self.Husband_Name, self.Wife_ID, self.Wife_Name, self.Children


class Repository:
    def __init__(self):
        self.person_container = dict()
        self.famliy_container = dict()
        self.individuals = dict()
        self.families = dict()

    def ged_file_reader(self):
        try:
            fp = open('proj03_testfile_hogwarts.ged', 'r')
        except FileNotFoundError:
            print(f'File cannot be opened.')
        else:
            indi_date = ["BIRT", "DEAT"]
            indi_no_date = ["NAME", "SEX", "FAMC", "FAMS"]
            fam_date = ["MARR", "DIV"]
            fam_no_date = ["HUSB", "WIFE", "CHIL"]
            indi_id = ''
            fam_id = ''
            date_item = ''

            for line in fp:
                word = line.strip().split()
                if word[0] == '0':
                    if word[-1] == 'INDI':
                        indi_id = word[1]
                        self.person_container[indi_id] = {}
                    elif word[-1] == 'FAM':
                        fam_id = word[1]
                        self.famliy_container[fam_id] = {}
                    else:
                        pass
                elif word[0] == '1':
                    if word[1] in indi_no_date:
                        self.person_container[indi_id][word[1]] = " ".join(word[2:])
                    elif word[1] in fam_no_date:
                        self.famliy_container[fam_id][word[1]] = " ".join(word[2:])
                    else:
                        date_item = word[1]
                elif word[0] == '2':
                    if date_item in indi_date:
                        self.person_container[indi_id][date_item] = " ".join(word[2:])
                    elif date_item in fam_date:
                        self.famliy_container[fam_id][date_item] = " ".join(word[2:])
                    else:
                        pass
                else:
                    pass

            # print(self.person_container)
            # print(self.famliy_container)

    def get_individual(self):
        for indi_id in self.person_container.keys():
            self.individuals[indi_id] = Individual(indi_id)
            self.individuals[indi_id].add_name(self.person_container[indi_id]['NAME'])
            self.individuals[indi_id].add_gender(self.person_container[indi_id]['SEX'])
            self.individuals[indi_id].add_birthday(self.person_container[indi_id]['BIRT'])
            if 'DEAT' in self.person_container[indi_id]:
                self.individuals[indi_id].add_death(self.person_container[indi_id]['DEAT'])
                self.individuals[indi_id].get_alive()
            else:
                self.individuals[indi_id].add_death('NA')
            if 'FAMC' in self.person_container[indi_id]:
                self.individuals[indi_id].add_child(self.person_container[indi_id]['FAMC'])
            else:
                self.individuals[indi_id].add_child('{}')
            if 'FAMS' in self.person_container[indi_id]:
                self.individuals[indi_id].add_spouse(self.person_container[indi_id]['FAMS'])
            else:
                self.individuals[indi_id].add_spouse('{}')
            self.individuals[indi_id].get_age()

    def get_family(self):
        for fam_id in self.famliy_container.keys():
            self.families[fam_id] = Family(fam_id)
            self.families[fam_id].add_married(self.famliy_container[fam_id]['MARR'])
            if 'DIV' in self.famliy_container[fam_id]:
                self.families[fam_id].add_divorced(self.famliy_container[fam_id]['DIV'])
            else:
                self.families[fam_id].add_divorced('NA')
            if 'HUSB' in self.famliy_container[fam_id]:
                self.families[fam_id].add_husband_id(self.famliy_container[fam_id]['HUSB'])
                self.families[fam_id].add_husband_name(self.person_container[self.famliy_container[fam_id]['HUSB']]['NAME'])
            else:
                self.families[fam_id].add_husband_id('NA')
                self.families[fam_id].add_husband_name('NA')
            if 'WIFE' in self.famliy_container[fam_id]:
                self.families[fam_id].add_wife_id(self.famliy_container[fam_id]['WIFE'])
                self.families[fam_id].add_wife_name(self.person_container[self.famliy_container[fam_id]['WIFE']]['NAME'])
            else:
                self.families[fam_id].add_wife_id('NA')
                self.families[fam_id].add_wife_name('NA')
            if 'CHIL' in self.famliy_container[fam_id]:
                self.families[fam_id].add_children(self.famliy_container[fam_id]['CHIL'])
            else:
                self.families[fam_id].add_children('{}')

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
    test.ged_file_reader()
    test.get_individual()
    test.table_individual()
    test.get_family()
    test.table_family()


if __name__ == '__main__':
    main()


