# INET4031 Add Users Script and User List

## Program Description

This program automates the process of creating Linux user accounts from an input file. Normally, a system administrator would manually use commands such as `adduser` and `passwd` to create accounts and set passwords for each user. This script uses those same commands but executes them automatically by reading from a structured input file. This allows multiple users to be created quickly, consistently, and with less manual effort.

## Program User Operation

This program reads user data from an input file and processes each line to create user accounts, set passwords, and assign group memberships.

### Input File Format

Each line in the input file must follow this format:

username:password:last:first:groups

- `username` → the login name of the user  
- `password` → the user’s password  
- `last` → last name  
- `first` → first name  
- `groups` → comma-separated list of groups  

If a line begins with `#`, it is treated as a comment and skipped.

If a user should not be added to any groups, use `-` in the groups field.

### Command Execution

To run the program:

sudo ./create-users.py < create-users.input

The `<` symbol redirects the contents of the input file into the program as standard input.

The script may need executable permissions:

The `<` symbol redirects the contents of the input file into the program as standard input.

The script may need executable permissions:

### "Dry Run"

A dry run allows the user to test the script without actually creating accounts. This is done by commenting out the `os.system(cmd)` lines and enabling `print(cmd)` instead. This will display the commands that would be executed without making any system changes.
