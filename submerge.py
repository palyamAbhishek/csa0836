def merge_and_sort(list1, list2):
    
    merged_list = list1 + list2
    
    sorted_list = sorted(merged_list)
    
    return sorted_list

list1 = [3, 6, 1, 8, 2]
list2 = [5, 9, 4, 7, 0]
merged_and_sorted = merge_and_sort(list1, list2)
print("Merged and Sorted List:", merged_and_sorted)
