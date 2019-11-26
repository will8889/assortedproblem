def is_member(data, list_of_data:list):
    if list_of_data.__contains__(data):
        return True
    return False
print(is_member(1,[1,2,3]))