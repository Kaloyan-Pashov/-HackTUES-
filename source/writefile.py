sets = [130, 90, 0, 65, 240, 0, 3600, 0, 0]
f = open("settings.txt", 'w')

for x in sets:
    f.write(str(x) + '\n')
