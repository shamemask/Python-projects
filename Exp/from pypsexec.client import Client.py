import subprocess
import sys
import datetime
import os

dt = datetime.datetime.now()
datetime = dt.strftime("%d-%m-%Y-%H-%M")


# creating new file
output = open('subjects.txt', 'wt', encoding="utf-8")
# Writing a computer name within the file created
output.write("u43024")
output.close()
# Reading file path
path = output.name

# Running psexec in each pc with the names within the file previously created
# run = subprocess.Popen(["psexec", "-d", "-c", "\\\\10.100.24.28", "-u", "eapteka\\d.artamonov2",  "-p", "Df4kq-poECW1",
#                        "-h", "-s", "-f", "C:\\Users\\dartamonov\\Documents\\Git\\Python\\Python\\junior\\subjects.txt"], stdout=sys.stdout)
# run = subprocess.Popen(["net view \\\\10.100.24.28"], stdout=sys.stdout)
# run.communicate()
cmd = "C:/Windows/System32/net.exe view \\\\10.100.24.28"

result = subprocess.check_output(cmd, shell=True, text=True)

result = result.split('\n')
print(result[7].split(' ')[0])
