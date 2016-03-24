# Script to grep successful logins from SAMBA logins

# Regular Expressions
import re
# Pretty Print
import pprint
# Sub process
import subprocess

# From /var/log/samba grep for successful logins
grep = 'zgrep -B 1 -e "authentication for user.*succeeded" *'
cmd = subprocess.Popen(grep, shell=True, stdout=subprocess.PIPE)

# Loop through rows of grep using a regular expression to pull usernames
usernamesList = []
for row in cmd.stdout:
    username = re.search( '(\[)(\w+)(\])', row)
    if username:
        usernamesList.append(username.group(2))

# Create set (only unique values) from list so we can count the number of times a name came up
usernamesSet = set(usernamesList)
# Create a list of tuples to hold name and count in each list item
usernamesTuples = []
for name in usernamesSet:
    count = usernamesList.count(name)
    usernamesTuples.append((name, count))

# Sort results from most logins to least logins
usernamesTuples = sorted(usernamesTuples, key=lambda name: name[1], reverse=True)

# Print the output using Pretty Print
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(usernamesTuples)
