import re
codes={'TTT':'F', 'TTC':'F','TTA':'L','TTG':'L',
       'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
       'TAT':'Y','TAC':'Y','TAA':'O','TAG':'U',
       'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
       'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
       'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
       'CAT':'H','CAC':'H','CAA':'Q','CAG':'Z',
       'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
       'ATT':'I','ATC':'I','ATA':'J','ATG':'M',
       'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
       'AAT':'N','AAC':'B','AAA':'K','AAG':'K',
       'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
       'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
       'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
       'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
       'GGT':'G','GGC':'G','GGA':'G','GGG':'G',}
print('please input a file name and the name should end with ".fa"')
nameinput = input()
protein = open(nameinput,'w')
unknown_DNA = open('unknown_function.fa')
for line in unknown_DNA:
    if re.findall('\d+',line):

        all = str(line)
        an = all.split(' ')
        name = an[0]
#since the data is well selected, so it is okay to just devided 3
        length= int(an[1])/3

        key = str(name)
        protein.write(name)
        protein.write(' ')
        protein.write(str(int(length)))
        protein.write('\n')
    else:
       z = {}
#the same thoughts as the last assignments to operate the translation
       a = -1
       for i in range(3, len(line) + 1, 3):
                  a = a + 1
                  origin = line[:i]
                  z[a] = origin[-3:]
       amino_acid =''
       for i in range(0, a+1):
         amino_acid = amino_acid + codes[z[i]]
       protein.write(str(amino_acid))
       protein.write('\n')

