#1.5版本后添加
import re

line="cats are smarter than dogs"

matchobj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
serchobj=re.search(r'(.*) are (.*?) .*',line,re.M|re.I)

if matchobj:
    print(matchobj.group())
    print(matchobj.group(1))
    print(matchobj.group(2))
else:
    print("not match!!")

