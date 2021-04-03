import re
xfile= open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

infor={}
for line in xfile:
 if line.startswith('>'):
  key = str(line)
  infor[key]=''
 else:
  infor[key] = infor[key]+line.replace('\n','')

important = open('unknown_function.fa','w')
for key in infor:
    if re.search('unknown',key):
        name = re.findall(r'gene:(\S+)\s', key)
        key1 = str(name).replace("['", '')
        key2 = key1.replace("']", '')
        #print(key2, len(infor[key]))
        #print(infor[key])
        important.write(key2)
        important.write(' ')
        important.write(str(len(infor[key])))
        important.write('\n')
        important.write(infor[key])
        important.write('\n')




#if re.search('unknown',line):
   #name = re.findall(r'gene:(\w+)', line)
   #print(name)