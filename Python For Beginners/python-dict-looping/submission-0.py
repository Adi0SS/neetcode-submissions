from typing import Dict, List # this adds type hints for List and Dict

def get_dict_keys(age_dict: Dict[str, int]) -> List[str]:
    my_List = []
    for key in age_dict:
        my_List.append(key)
    return my_List    
        

    

def get_dict_values(age_dict: Dict[str, int]) -> List[int]:
    my_List = []
    for key,value in age_dict.items():
        my_List.append(value)
    return my_List    

# do not modify below this line
dict_1 = {"John": 25, "Doe": 30, "Jane": 22}
dict_2 = {"NeetCode": 24, "NeetCode2": 25, "NeetCode3": 26}

print(get_dict_keys(dict_1))
print(get_dict_keys(dict_2))

print(get_dict_values(dict_1))
print(get_dict_values(dict_2))
