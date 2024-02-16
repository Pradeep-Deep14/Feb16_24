import re
x=re.compile(r'\W')
y=x.findall('clcoding')
print(y)