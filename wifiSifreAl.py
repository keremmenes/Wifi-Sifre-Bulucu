import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('latin1').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('latin1').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

File = open("Password", "w")
for i in range(len(results)):

    
    line = profiles[i] + " :       " + results[i] + "\n"
    File.write(line)
    
"""    try:
        print ("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}|  {:<}".format(i, ""))
input("")"""