#! python3
# A password locker program 
import pyperclip
PASSWORDS = {'email': 'sjkdfhdjkfhufhuweirhbfhsfkj',
             'blog': 'tyauvdhvufvcshdvuerwioeryo',
             'luggage': '12345'}

import sys
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print("There is no account named " + account)