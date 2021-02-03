list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


def merge_two_list(list):
    even=[]
    odd=[]
    mergeTwoList=[]
    for num in list:
        if num % 2 == 0:
            even.append(num)
        else:
           odd.append(num)
    mergeTwoList.append(odd)
    mergeTwoList.append(even)
    
    return mergeTwoList

print(merge_two_list(list_of_numbers))

