
import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
#print('Phone number found: ' + mo.group())
areaCode, prefix, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)