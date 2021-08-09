import os
#import shutil
#import pathlib


print("\n\n***************Cloning repository*****************\n")
path  = "C:\Dev\Projects" 
clone = "git clone https://github.com/BenAmeurYesmine/LED_BLINK.git" 

#os.system("sshpass -p your_password ssh user_name@your_localhost")
os.chdir(path) # Specifying the path where the cloned project needs to be copied
os.system(clone) # Cloning

print("\n\n***************Debuging program*****************\n")
current_dir = os.path.dirname(os.path.abspath(__file__))   # Can also use os.getcwd()
#print(current_dir)                                         # prints(say)- D:\abc\def\ghi\jkl\mno"
os.chdir('C:\Dev\Projects\LED_BLINK\Debug')                         
#print("Current working directory: {0}".format(os.getcwd()))
current_dir = os.getcwd()   # Can also use os.getcwd()
#print(current_dir)  
os.system("make -j8 all")

print("\n\n***************Deleting program*****************\n")

os.chdir('C:\Dev\Projects')       
current_dir = os.getcwd()   # Can also use os.getcwd()
os.system("rmdir /s LED_BLINK")