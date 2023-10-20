def remove_even(lst):
    indexes_to_remove = []  # 存儲需要刪除的元素索引
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            indexes_to_remove.append(i)
            print("The indexes_to_remove should be ",indexes_to_remove)
    # 反向迭代，並一次性刪除元素
    for i in reversed(indexes_to_remove):
        lst.pop(i)
        print("The lst should be ",lst)
    
    return lst

my_list = [1, 2, 4, 5, 10, 6, 3]
new_list = remove_even(my_list)
print(new_list)