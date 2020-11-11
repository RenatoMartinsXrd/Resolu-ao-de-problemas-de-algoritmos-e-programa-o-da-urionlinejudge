import re
n = int(input())
p = re.compile('[a-z]+')
for x in range(n):
	string = input()
	print("".join(p.findall(string))[::-1])