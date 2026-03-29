#!/usr/bin/python3

# INET4031
# Your Name
# Date Created
# Date Last Modified

# Import modules:
# os → allows execution of system commands (like adduser, passwd)
# re → used for pattern matching (detecting comments in input file)
# sys → used to read input from stdin (the redirected input file)
# import os
# import re
# import sys

def main():
    # Loop through each line of input from the input file (stdin)
    for line in sys.stdin:

        # Check if the line starts with '#' (used to mark comments/skip lines)
        match = re.match("^#", line)

        # Split the line into fields using ':' delimiter
        # Expected format: username:password:last:first:groups
        fields = line.strip().split(':')

        # Skip the line if:
        # 1. It is a comment (starts with '#')
        # 2. It does not contain exactly 5 fields (invalid input)
        if match or len(fields) != 5:
            continue

        # Extract user information from fields
        # gecos field is used in /etc/passwd for storing user info (Full Name)
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split groups by comma (user may belong to multiple groups)
        groups = fields[4].split(',')

        # Inform user that account creation is starting
        print("==> Creating account for %s..." % (username))

        # Build command to create user without password login
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Dry run → print instead of execute
        # Real run → uncomment below
        print(cmd)
        # os.system(cmd)

        # Inform user password is being set
        print("==> Setting the password for %s..." % (username))

        # Build command to set password using echo and passwd
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        print(cmd)
        # os.system(cmd)

        # Loop through each group and assign user
        for group in groups:
            # Skip if group is '-' (means no group assignment)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build command to add user to group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                print(cmd)
                # os.system(cmd)

if __name__ == '__main__':
    main()
