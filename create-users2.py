#!/usr/bin/python3

# INET4031
# Tyler Hoffman
# Date Created: (put date)
# Date Last Modified: (put date)

# os -> runs Linux system commands
# re -> checks for comment lines beginning with '#'
# sys -> reads lines from standard input
import os
import re
import sys

def main():
    # Ask user whether to do a dry run or a real run
    mode = input("Run in dry-run mode? Enter Y for yes or N for no: ").strip().upper()

    # dry_run is True if user entered Y
    dry_run = (mode == "Y")

    # Process each line from the redirected input file
    for line in sys.stdin:

        # Check whether the line starts with '#'
        match = re.match("^#", line)

        # Split the input line into fields separated by ':'
        fields = line.strip().split(':')

        # Skip comment lines
        if match:
            if dry_run:
                print("Skipping commented line:", line.strip())
            continue

        # Skip lines that do not have exactly 5 fields
        if len(fields) != 5:
            if dry_run:
                print("Error: line does not contain 5 fields:", line.strip())
            continue

        # Store values from the input line
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group list into separate groups
        groups = fields[4].split(',')

        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        if dry_run:
            print(cmd)
        else:
            os.system(cmd)

        # Add user to groups unless group field is '-'
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()