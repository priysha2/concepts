#!/user/bin/env python 
import re
mystr = "you can learn any language"
a = re.search("new",mystr) 
b = re.match("you",mystr,re.IGNORECASE)
print (a)
print (b.group())
arp = "10.10.10.10  0 gd:dd:ss:34:  VLAN22#"
c  = re.match(r"(.+?) +(/d) +(.+?),{2,}(\w)*",arp)
