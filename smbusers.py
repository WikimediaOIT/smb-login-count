import re
import pprint
import subprocess

grep = 'zgrep -B 1 -e "authentication for user.*succeeded" *'
cmd = subprocess.Popen(grep, shell=True, stdout=subprocess.PIPE)

usernamesList = []
for row in cmd.stdout:
    #username = re.match( r'(\[)(\w+)(\])', row, re.M|re.I)
    username = re.search( '(\[)(\w+)(\])', row)
    if username:
        usernamesList.append(username.group(2))

usernamesSet = set(usernamesList)
usernamesTuples = []
for name in usernamesSet:
    count = usernamesList.count(name)
    usernamesTuples.append((name, count))

usernamesTuples = sorted(usernamesTuples, key=lambda name: name[1], reverse=True)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(usernamesTuples)
