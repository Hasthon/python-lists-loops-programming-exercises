my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

""" total=sum(my_list)/len(my_list) """


""" print(total) """

aux=0

for i in my_list:
    aux = i + aux

print(aux/len(my_list))
