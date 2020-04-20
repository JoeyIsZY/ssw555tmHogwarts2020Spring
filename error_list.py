from prettytable import PrettyTable
from us01 import us01_current_date_check
from us07 import us07_not_olderthan150
from us02 import us02_birth_before_marriage
from us03 import us03_birth_before_death
from us04 import us04_marriage_before_divorce
from us05 import us05_marriage_before_death
from us08 import us08_birth_before_marriage
from us09 import us09_birth_after_death
from us17 import us17_no_marriages_to_children
from us18 import us18_no_marriages_between_siblings
from us06 import us06_divorce_before_death
from us12 import us12_parents_not_too_old
from us10 import us10_marriage_after_14
from us11 import us11_no_bigamy
from us15 import us15_more_than_15siblings
from us16 import us16_same_male_surname
from us13 import us13_sibling_spacing
from us14 import us14_multiple_births
from us23 import us23_unique_name_birth_date
from us24 import us24_unique_families_by_spouses
from us19 import us19_first_cousin_not_marry
from us20 import us20_a_u_marry_n_n
from us21 import us21_correct_gender_for_role
from us25 import us25_unique_first_names_in_families

def pretty_error(repo):
    """This function is used to collect and print all error messages.
        Please make sure your us function return a list made of tuples.
        The format of the tuple should be ((ERROR or ANOMALY), object type, USID, line(just select the most important line),
         object id, error message(use your own language to describe the error. You also could learn from the TeamXXReport.xlsx))
         Written by Haodong Wu      02/18/2020"""

    errors_list = []
    errors_list += us01_current_date_check(repo)
    # us01 in Sprint1 by Haodong Wu     02/18/2020
    errors_list += us07_not_olderthan150(repo)
    # us07 in Sprint1 by Haodong Wu     02/18/2020
    errors_list += us02_birth_before_marriage(repo)
    # us02 in Sprint1 by Ying Hu 2/24/2020
    errors_list += us03_birth_before_death(repo)
    # us03 in Sprint1 by Ying Hu 2/24/2020
    errors_list += us04_marriage_before_divorce(repo)
    # us04 in Sprint1 by Yu Zhou 2/26/2020
    errors_list += us05_marriage_before_death(repo)
    # us05 in Sprint1 by Yu Zhou 2/26/2020
    errors_list += us08_birth_before_marriage(repo)
    # us08 in Sprint1 by Fangji Liang Zhou 2/28/2020
    errors_list += us09_birth_after_death(repo)
    # us09 in Sprint1 by Fangji Liang Zhou 2/28/2020
    errors_list += us17_no_marriages_to_children(repo)
    # us17 in Sprint2 by Haodng Wu  25/02/2020
    errors_list += us18_no_marriages_between_siblings(repo)
    # us06 in Sprint2 by Ying Hu  15/03/2020
    errors_list += us06_divorce_before_death(repo)
    # us12 in Sprint2 by Ying Hu  15/03/2020
    errors_list += us12_parents_not_too_old(repo)
    # us10 in Sprint2 by Yu Zhou  18/03/2020
    errors_list += us10_marriage_after_14(repo)
    # us11 in Sprint2 by Yu Zhou  18/03/2020
    errors_list += us11_no_bigamy(repo)
    # us15 in Sprint2 by Fangji Liang 22/03/2020
    errors_list += us15_more_than_15siblings(repo)
    # us16 in Sprint2 by Fangji Liang 22/03/2020
    errors_list += us16_same_male_surname(repo)
    # us13 in Sprint3 by Yu Zhou 4/4/2020
    errors_list += us13_sibling_spacing(repo)
    # us24 in Sprint3 by Yu Zhou 4/4/2020
    errors_list += us14_multiple_births(repo)
    # us23 in Sprint3 by Ying Hu 3/30/2020
    errors_list += us23_unique_name_birth_date(repo)
    # us24 in Sprint3 by Ying Hu 3/30/2020
    errors_list += us24_unique_families_by_spouses(repo)
    # us19 in Sprint3 by Fangji Liang 06/04/2020
    errors_list += us19_first_cousin_not_marry(repo)
    # us20 in Sprint3 by Fangji Liang 06/04/2020
    errors_list += us20_a_u_marry_n_n(repo)
    # us21 in Sprint3 by Fangji Liang 06/04/2020
    errors_list += us21_correct_gender_for_role(repo)
    # us25 in Sprint3 by Fangji Liang 06/04/2020
    errors_list += us25_unique_first_names_in_families(repo)
    
    pt_labels = ['Index', 'ERROR/ANOMALY', 'Data Type', 'User Story Number', 'Line', 'Error ID', 'Error Message']
    pt = PrettyTable(field_names=pt_labels)
    pt.padding_width = 1
    for index, (error_type, data_type, userstory_number, line, error_id, error_message) in enumerate(errors_list,
                                                                                                     start=1):
        pt.add_row((index, error_type, data_type, userstory_number, line, error_id, error_message))

    return f"\nCHECKING ERRORS AND ANOMALIES\n{pt}"