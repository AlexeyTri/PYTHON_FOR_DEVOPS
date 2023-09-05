#!.env/bin/python

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
   ...: Rostam Batmanglij <rostam@vpwk.com>,
   ...: Chris Tomson <ctomson@vpwk.com,
   ...: Bobbi Baio <bbaio@vpwk.com'''


import re

match = re.search(r'[A-Za-z]+', cc_list)
print(f'''First exemple {match}''')

match = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
print(f'''Second example. All names: {match.group("name")}''')

match = re.finditer("(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)", cc_list)
for m in match:	
	print(m.groupdict())
