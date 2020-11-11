import re
string = input()
p = re.compile('zelda', re.IGNORECASE)
if p.search(string):
    print("Link Bolado")
else:
    print("Link Tranquilo")
