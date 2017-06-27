import os
import re

folder = 'wiki/Recipes/'

next = folder + 'next.txt'

links = os.listdir(folder)

links.sort()

p = re.compile("_")

f = open('index.md', 'w')

for string in links:
   nstr = p.sub(' ', string)[0:-3]
   f.write("[" + nstr + "](" + folder + string + ") \n")
   f.write("\n")
