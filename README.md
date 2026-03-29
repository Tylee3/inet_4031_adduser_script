# INET4031 Add Users Script and User List

## Program Description

This program helps automate the process of adding multiple users to a Linux system. Instead of manually entering commands for each new account, the script reads user information from an input file and creates the accounts automatically. This saves time, reduces mistakes, and makes the process more efficient when many users need to be added.

Normally, a system administrator would need to use commands such as `adduser` to create a user account, `passwd` to set the user’s password, and `adduser <username> <group>` to place a user into a group. This script automates those ***SAME COMMANDS*** by building and running them from the data in the input file.

## Program User Operation

This program works by reading lines from the `create-users.input` file through standard input. Each valid line contains the information needed to create one user account, set that user’s password, and assign the user to one or more groups. The script skips invalid lines and can also skip lines intentionally marked as comments. To use the program successfully, the user must prepare the input file correctly, make the Python script executable, and then run it with input redirection.

### Input File Format

Each line in the input file must contain five fields separated by colons in this format:

`username:password:last:first:groups`

The first field is the username for the new account. The second field is the password that will be assigned to that user. The third and fourth fields are the user’s last name and first name, which are used to build the GECOS information stored with the account. The fifth field is a comma-separated list of groups the user should be added to.

If the user wants to skip a line in the input file, they should place a `#` character at the beginning of that line. The script recognizes that as a comment and skips it.

If the user does not want a new user added to any groups, they should place `-` in the groups field.

### Command Excuction

Before running the script, the user may need to make it executable with the following command:

`chmod +x create-users.py`

The script can then be run with:

`./create-users.py < create-users.input`

The `<` symbol redirects the contents of the input file into the script so the Python code can read each line through standard input.

### "Dry Run"

A dry run allows the user to test the script without actually making changes to the system. During a dry run, the commands that would normally create users, set passwords, and assign groups are printed to the screen instead of being executed. This helps the user confirm that the script is working correctly before running it for real. Once the dry run shows no errors, the command lines can be uncommented and the script can be run normally with `sudo`.
