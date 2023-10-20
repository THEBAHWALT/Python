def find_sum(lst, k):
    # Write your code here
    new_lst = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            target = lst[i] + lst[j]
            if target == k:
                new_lst.append(lst[i])
                new_lst.append(lst[j])
                break
    return new_lst

lst = [1,21,3,14,5,60,7,6]
k = 81
new_lst = find_sum(lst, k)