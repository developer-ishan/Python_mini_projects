#! python3
#password_locker.py - An insecure password locker program.

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python password_locker [account] - copy account password')
    sys.exit()

"""The first item in the sys.argv list should always be a string
containing the program’s filename ('password_locker.py'), and the second item should
be the first command line argument."""

account = sys.argv[1] #first command line argument is the account name

if account in PASSWORDS.keys():
    pyperclip.copy(PASSWORDS[account])
    print('Password for '+account+ ' copied to the clipboard.')
else:
    print('There is no account named '+account)