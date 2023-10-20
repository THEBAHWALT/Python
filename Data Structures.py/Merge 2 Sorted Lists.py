def merge_lists(lst1, lst2):
    # Write your code here
    for item in lst2:
        lst1.insert(-1,item)
    lst1.sort()
    print("new_list is ",lst1)
    return lst1
lst1 = [1, 3, 4, 5]
lst2 = [2, 6, 7, 8]
new_list = merge_lists(lst1, lst2)
