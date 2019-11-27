def is_member(list_a:list,list_b:list):
    for data_a in list_a:
        if list_b.__contains__(data_a):
            return True
    return False

print(is_member([12,4],[31,4]))