my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello = []

for item in my_list:
    if type(item) == list or type(item)==dict:
        hello.append(item)
#your code go here:

print(hello)