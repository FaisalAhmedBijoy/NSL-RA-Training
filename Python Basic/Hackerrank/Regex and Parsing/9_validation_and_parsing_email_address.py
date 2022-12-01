
"""
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

import email.utils
print email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>')
print email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com'))

('DOSHI', 'DOSHI@hackerrank.com')
DOSHI <DOSHI@hackerrank.com>
"""

import re
import email.utils

n = int(input())
pattern=r'^[a-zA-Z][\w\.\-\_]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
for _ in range(n):    
    name,email_address= email.utils.parseaddr(input())
    # print (name)
    # print(email_address)
    if re.match(pattern,email_address):
        print(email.utils.formataddr((name,email_address)))
