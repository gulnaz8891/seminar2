val = {"q" : 1, "w" : 2, "r" : 3}
try:
    print(val["e"])
except KeyError:
    print("KeyError encountered")
print(val.get("e"))

item = [1, 2, 3, 4]
try:
    item[6]
except IndexError:
    print("Index is not in the list!")

try:
    f = open('myfile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('file not found')
