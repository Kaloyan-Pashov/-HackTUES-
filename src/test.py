import subprocess
subprocess.Popen([r"test.exe"])

f = open("test.txt", 'r')
a = f.readline()
f.close()
f = open("test.txt", 'w')
f.write('')
f.close()
print(a)
