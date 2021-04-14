seq = 'ATGCGACTACGATCGAGGGCC'
codes={'TTT':'F', 'TTC':'F','TTA':'L','TTG':'L',
       'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
       'TAT':'Y','TAC':'Y','TAA':'O','TAF':'U',
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
z={}
a=-1
for i in range(3,len(seq)+1,3):
       a=a+1
       origin = seq[:i]
       z[a]=origin[-3:]

amino_acid =''
for i in range(0,a):
 amino_acid = amino_acid + codes[z[i]]

print(str(amino_acid))

