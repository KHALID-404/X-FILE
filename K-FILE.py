import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
bit = platform.architecture()[0]
 
if bit == "64bit":
        os.system('xdg-open https://youtube.com/@Khalid_Vau')
 
        from KHALID import approval
 
        approval()
 
 
 
elif bit == "32bit":
 
        os.system('xdg-open https://youtube.com/@Khalid_Vau')
 
        os.system('python file_enc.py')
