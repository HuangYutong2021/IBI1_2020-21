
def transformation(i):
 code = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
 re = str(i)
 record = re.upper()
 se = ''
 for a in range(0,len(i)):
  one = record[a:a+1]
  se += str(code[one])

 for a in range(0,len(i)):
  print(se[len(i)-1-a:len(i)-a],end='')


sequence = input()
transformation(sequence)
