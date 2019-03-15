sets = {'somesets': True, 'numbersets': 8,}
f = open("settings.txt", 'w')

for x in sets.keys():
    f.write(x + '\n')
    f.write(str(sets[x]) + '\n')
