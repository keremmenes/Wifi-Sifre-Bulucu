import subprocess

giris = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin1').split('\n')
isim = [i.split(":")[1][1:-1] for i in giris if "All User Profile" in i]

File = open("Password", "w")

for i in isim:
    sifre = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('latin1').split('\n')
    sifre = [b.split(":")[1][1:-1] for b in sifre if "Key Content" in b]
    
    try:
        File.write ("{:<30}|  {:<} \n".format(i, sifre[0]))
    except :
        File.write ("{:<30}|  {:<} \n".format(i, ""))