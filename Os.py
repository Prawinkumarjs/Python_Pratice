import os
from os import path
os.makedirs(name="LEO_DAS",exist_ok=True)
print(os.system('dir'))
sampath =r'C:\Users\WELCOME\Pictures\Camera Roll'
print(path.exists(sampath))
print(path.basename(sampath))
print(path.expanduser('~\~/BEN10'))
print(path.dirname(sampath))
print(os.getcwd())
print(os.getlogin())
os.chdir(r'C:\Users\WELCOME\Desktop\Python')