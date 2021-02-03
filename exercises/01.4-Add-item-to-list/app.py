import random 

my_list = [4,5,734,43,45]

def generate_random_list():
    for i in range(10):
        randonlength = random.randint(1, 100)
        my_list.append(randonlength)
    return my_list
generate_random_list()
print(my_list)