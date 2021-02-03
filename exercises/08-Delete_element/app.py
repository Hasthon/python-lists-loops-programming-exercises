people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    new_people=[]
    for i in people:
        if i == person_name:
            continue
        else:
            new_people.append(i)
        
    return new_people
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))