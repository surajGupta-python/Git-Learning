nested_list = [2, 4, [12, 5], [10, [9, 11]], 17]



def flatten_list(arr):
    flatten_arr = []
    for ele in arr:
        if isinstance(ele, list):
            flatten_arr.extend(flatten_list(ele))
        else:
            flatten_arr.append(ele)
    return flatten_arr

result = flatten_list(nested_list)
print(result)


def func(*args):
    pass