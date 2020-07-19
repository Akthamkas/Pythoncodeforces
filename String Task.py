import re
string = input().lower()
result = re.findall('[^aeyiou]',string,flags=re.IGNORECASE)
print('.'+'.'.join(result))