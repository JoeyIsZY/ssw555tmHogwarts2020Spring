from prettytable import PrettyTable
from us35 import us35_list_recent_births
from us36 import us36_list_recent_deaths
from us29 import us29_list_deceased
from us30 import us30_list_living_married
from us31 import us31_list_living_single
from us32 import us32_list_mutiple_births
from us34 import us34_large_age_couple
from us33 import us33_list_orphans

def pretty_special(repo):
    """This function is used to collect and print all special groups and special individuals.
        Please make sure your us function return a tuple with two elements.
        The format of the tuple should be (the characteristic, the list of ids)
        Written by Haodong Wu      04/10/2020"""
    special_list = []
    special_list.append(us35_list_recent_births(repo))
    # us35 in Sprint4 by Haodong Wu 10/04/2020
    special_list.append(us36_list_recent_deaths(repo))
    # us36 in Sprint4 by Haodong Wu 10/04/2020
    special_list.append(us29_list_deceased(repo))
    # us29 in Sprint4 by Ying Hu 11/04/2020
    special_list.append(us30_list_living_married(repo))
    # us30 in Sprint4 by Ying Hu 11/04/2020
    special_list.append(us31_list_living_single(repo))
    # us31 in Sprint4 by Yu Zhou 18/04/2020
    special_list.append(us32_list_mutiple_births(repo))
    # us32 in Sprint4 by Yu Zhou 18/04/2020
    special_list.append(("orphan children", list(us33_list_orphans(repo))))
    # us33 in Sprint4 by Fangji Liang 19/04/2020
    special_list.append(("Spouses whose age difference is more than twice", list(us34_large_age_couple(repo))))
    # us34 in Sprint4 by Fangji Liang 19/04/2020

    pt_labels = ['Index','Characteristics', 'IDs of individuals or groups with this characteristic']
    pt = PrettyTable(field_names=pt_labels)
    for index, (Characteristics, ids) in enumerate(special_list,start=1):
        pt.add_row((index, Characteristics,ids))

    return f"\nSPECIAL LISTS\n{pt}"
